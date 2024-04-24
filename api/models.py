from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)  # Define custom primary key field
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CarMake(models.Model):
    car_make_id = models.BigAutoField(primary_key=True, )  # Define custom primary key field
    car_company_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.car_company_name

class CarModel(models.Model):
    
    car_model_id = models.BigAutoField(primary_key=True,)  # Define custom primary key field
    car_model_name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    def __str__(self):
        return self.car_model_name

class EmployeeCar(models.Model):
    
    employee_car_id = models.BigAutoField(primary_key=True, )  # Define custom primary key field
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=7, unique=True, validators=[RegexValidator(r'^([A-Z]{2}[0-9]{3}[A-Z]{3})$')])
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_colour = models.CharField(max_length=50)