from rest_framework import serializers
from .models import Employee, CarMake, CarModel, EmployeeCar

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class EmployeeCarSerializer(serializers.ModelSerializer):
    car_model = CarModelSerializer()

    class Meta:
        model = EmployeeCar
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    employee_cars = EmployeeCarSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'employee_cars')

class CarMakeSerializer(serializers.ModelSerializer):
    car_models = CarModelSerializer(many=True, read_only=True)

    class Meta:
        model = CarMake
        fields = ('id', 'car_company_name', 'car_models')