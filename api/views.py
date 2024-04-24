from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import logging
from .forms import EmployeeCarForm, EmployeeForm, CarMakeForm, CarModelForm
from .models import EmployeeCar, CarMake, CarModel, Employee

# Create your views here.

def home(request):
    return render(request, 'home.html')


def get_updated_data(request):
    employee_cars = EmployeeCar.objects.all()
    data=[{'first_name':ec.employee.first_name, 'last_name':ec.employee.last_name,'number_plate': ec.number_plate, 'car_make': ec.car_make.car_company_name, 'car_model': ec.car_model.car_model_name, 'car_colour': ec.car_colour} for ec in employee_cars]
    #print(data)
    return JsonResponse(data, safe=False)

def administration(request):
    if request.method == 'POST':
        # Check password
        password = request.POST.get('password', '')
        if password != '@Admin123':
            return render(request, 'administration.html', {'error': 'Incorrect password'})

        # Handle form submissions
        if 'employee_car_form' in request.POST:
            employee_car_form = EmployeeCarForm(request.POST)
            if employee_car_form.is_valid():
                employee_car_data = employee_car_form.cleaned_data
                try:
                    employee_car = EmployeeCar.objects.create(**employee_car_data)
                    return redirect('/api/mainchecker')
                except Exception as e:
                    return render(request, 'administration.html', {'error': str(e)})

        elif 'employee_form' in request.POST:
            employee_form = EmployeeForm(request.POST)
            if employee_form.is_valid():
                employee_data = employee_form.cleaned_data
                try:
                    employee = Employee.objects.create(**employee_data)
                    return redirect('/api')
                except Exception as e:
                    return render(request, 'administration.html', {'error': str(e)})

        elif 'car_make_form' in request.POST:
            car_make_form = CarMakeForm(request.POST)
            if car_make_form.is_valid():
                car_make_data = car_make_form.cleaned_data
                try:
                    car_make = CarMake.objects.create(**car_make_data)
                    return redirect('/api/carview')
                except Exception as e:
                    return render(request, 'administration.html', {'error': str(e)})

        elif 'car_model_form' in request.POST:
            car_model_form = CarModelForm(request.POST)
            if car_model_form.is_valid():
                car_model_data = car_model_form.cleaned_data
                try:
                    car_model = CarModel.objects.create(**car_model_data)
                    return redirect('/api/carview')
                except Exception as e:
                    return render(request, 'administration.html', {'error': str(e)})

    else:
        # Initialize forms
        employee_car_form = EmployeeCarForm()
        employee_form = EmployeeForm()
        car_make_form = CarMakeForm()
        car_model_form = CarModelForm()

        employees = Employee.objects.all()
        car_makes = CarMake.objects.all()
        car_models = CarModel.objects.all()

        return render(request, 'administration.html', {
            'employee_car_form': employee_car_form,
            'employee_form': employee_form,
            'car_make_form': car_make_form,
            'car_model_form': car_model_form,
            'employees': employees,
            'car_makes': car_makes,
            'car_models': car_models
        })
def mainChecker(request):
    employeeCars = EmployeeCar.objects.all()
    return render(request, 'mainchecker.html', {'employee_cars': employeeCars})

def viewCars(request):
    car_models = CarModel.objects.select_related('car_make').order_by('car_make__car_company_name')
    car_make_models = {}
    for car_model in car_models:
        car_make_name = car_model.car_make.car_company_name
        if car_make_name not in car_make_models:
            car_make_models[car_make_name] = []
        car_make_models[car_make_name].append(car_model.car_model_name)
    print(car_make_models)
    return render(request, 'viewCars.html', {'car_makes': car_make_models})

def health_check_view(request):
    logger = logging.getLogger(__name__)

    try:
        # Execute a simple query to check database connectivity
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result:
                status = "Database is healthy"
            else:
                status = "Database is not responding"
    except Exception as e:
        status = f"Error: {str(e)}"
        logger.error("Error occurred during database health check: %s", str(e))

    return JsonResponse({'status': status})