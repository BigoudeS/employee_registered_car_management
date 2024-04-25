# Employee Registered Car Management System

This Django project manages employee registration and their associated cars.

## Installation

1. Clone this repository to your local machine.

2. Install the required Python modules using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the directory where you want to create your Django project.

4. Run the following command to create a new Django project:

    ```bash
    django-admin startproject employee_registered_car_management
    ```

   Note: Make sure you run this command in the directory where you want to create the project. Do not run it inside the `api` folder or the inner `employee_registered_car_management` folder.

5. If the database is empty or if you want to reset it, delete the `db.sqlite3` file and run the following commands:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Set the Django settings module:

    For Windows:

    ```bash
    $env:DJANGO_SETTINGS_MODULE = "employee_registered_car_management.settings"
    ```

    For Unix/Linux/macOS:

    ```bash
    export DJANGO_SETTINGS_MODULE="employee_registered_car_management.settings"
    ```

7. Run the `populateData.py` script to populate the database with initial data:

    ```bash
    python populateData.py
    ```

## Usage

Once the installation is complete, you can run the Django development server using the following command:

```bash
python manage.py runserver
```

This will start the development server, and you can access the application in your web browser at http://localhost:8000/api.

The password to te administration page is "@Admin123"

