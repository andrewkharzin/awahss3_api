from django.urls import path
from .views import FlightProjectList

app_name = 'flight_scheduler.api'

urlpatterns = [
    path('scheduler/', FlightProjectList.as_view(), name='project_list'),
    
]
