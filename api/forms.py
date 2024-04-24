from django import forms
from .models import Employee, CarMake, CarModel, EmployeeCar

class EmployeeCarForm(forms.ModelForm):
    class Meta:
        model = EmployeeCar
        fields = ['employee', 'number_plate', 'car_make', 'car_model', 'car_colour']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']

class CarMakeForm(forms.ModelForm):
    class Meta:
        model = CarMake
        fields = ['car_company_name']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['car_model_name', 'car_make']