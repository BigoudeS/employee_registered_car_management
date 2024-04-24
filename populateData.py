import os
import django

import requests
import random
import json
from faker import Faker  # For generating random data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_registered_car_management.settings')
django.setup()

from api.models import Employee, CarMake, CarModel, EmployeeCar

# Fetch employee names from the provided JSON API
def fetch_employee_names():
    url = "https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json"
    response = requests.get(url)
    data = response.json()
    # Check if the 'characters' key exists in the JSON data
    if 'characters' in data:
        # Extract actor names and split them into first and last names
        names = []
        for char in data['characters'][:100]:
            if 'actorName' in char:
                actor_name = char['actorName']
                if ' ' in actor_name:
                    first_name, last_name = actor_name.split(maxsplit=1)
                    names.append({"first_name": first_name, "last_name": last_name})
        return names
    else:
        print("Error: 'characters' key not found in the JSON data")
        return []
    
# Generate random number plate in the format LLNNLLL
def generate_number_plate():
    fake = Faker()
    plate = fake.random_letter() + fake.random_letter() + \
            str(random.randint(10, 99)) + \
            fake.random_letter() + fake.random_letter() + fake.random_letter()
    return plate

# Generate random car color
def generate_car_color():
    fake = Faker()
    color = fake.color_name()
    return color

# Populate employee table
def populate_employee_table():
    names = fetch_employee_names()
    for name in names:
        first_name = name.get("first_name")
        last_name = name.get("last_name")
        Employee.objects.create(first_name=first_name, last_name=last_name)

# Function to populate car make table
def populate_car_make_table():
    with open('carData.json', 'r') as file:
        data = json.load(file)
        car_makes = data.get('car_makes', [])
        for make in car_makes:
            CarMake.objects.create(
                car_company_name=make.get('car_company_name')
            )

# Function to populate car model table
def populate_car_model_table():
    with open('carData.json', 'r') as file:
        data = json.load(file)
        car_models = data.get('car_models', [])
        for model_data in car_models:
            # Extract car make id from model data
            car_make_id = model_data.get('car_make_id')
            
            # Fetch the CarMake instance corresponding to the car_make_id
            car_make_instance = CarMake.objects.get(car_make=car_make_id)
            
            # Create the CarModel instance and assign the car make instance
            CarModel.objects.create(
                car_model_name=model_data.get('car_model_name'),
                car_make=car_make_instance
            )

# Populate employee car table
def populate_car_model_table():
    with open('carData.json', 'r') as file:
        data = json.load(file)
        car_models = data.get('car_models', [])
        for model_data in car_models:
            # Extract car make id from model data
            car_make_id = model_data.get('car_make_id')
            
            # Fetch the CarMake instance corresponding to the car_make_id
            car_make_instance = CarMake.objects.get(car_make_id=car_make_id)
            
            # Create the CarModel instance and assign the car make instance
            CarModel.objects.create(
                car_model_name=model_data.get('car_model_name'),
                car_make=car_make_instance
            )

# Populate employee car table
def populate_employee_car_table():
    employees = Employee.objects.all()
    car_models = CarModel.objects.all()
    car_makes = CarMake.objects.all()
    
    for i in range(5000, 5050):  # Start employee_car IDs from 5000
        employee = random.choice(employees)
        car_model = random.choice(car_models)
        car_make = random.choice(car_makes)
        number_plate = generate_number_plate()
        car_color = generate_car_color()
        EmployeeCar.objects.create(
            employee=employee, 
            number_plate=number_plate, 
            car_make=car_make,
            car_model=car_model, 
            car_colour=car_color
        )


# Run population functions
populate_employee_table()
populate_car_make_table()
populate_car_model_table()
populate_employee_car_table()
