from celery import shared_task
from .views import update_flight_info

@shared_task
def update_flight_info_task():
    update_flight_info()
