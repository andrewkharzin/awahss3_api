from django.urls import path
from .views import load_flight_data

urlpatterns = [
    path('svo/', load_flight_data, name='load_flight_data'),
]