from django.contrib import admin
from .models import Schedule
from .views import map_flight_data_to_schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_iata', 'arrival_iata')
    # ... other admin configurations ...

    actions = [map_flight_data_to_schedule]

admin.site.register(Schedule, ScheduleAdmin)
