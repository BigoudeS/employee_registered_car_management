from django.urls import path
from .views import home, administration, mainChecker, viewCars, get_updated_data, health_check_view

urlpatterns = [
    path('', home, name='home'),
    path('administration/', administration, name='administration'),
    path('mainchecker/', mainChecker, name='mainchecker'),
    path('viewcars/', viewCars, name='viewcars'),
    path('get_updated_data/', get_updated_data, name='get_updated_data'),
    path('health_check/', health_check_view, name='health_check'),
]
