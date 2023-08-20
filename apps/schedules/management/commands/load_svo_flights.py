# management/commands/load_svo_flights.py

from django.core.management.base import BaseCommand
import requests
from apps.schedules.models import Schedule
from apps.schedules.views import map_flight_data_to_schedule

class Command(BaseCommand):
    help = 'Load flight data for arrivals at SVO airport'

    def handle(self, *args, **options):
        access_key = '7c8a729991b6fefbfd9e89863279c947'
        arr_iata = 'SVO'
        api_url = f'http://api.aviationstack.com/v1/flights?access_key={access_key}&arr_iata={arr_iata}'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            for flight_data in data.get('data', []):
                schedule_data = map_flight_data_to_schedule(flight_data)
                schedule, created = Schedule.objects.update_or_create(
                    flight_number=schedule_data['flight_number'],
                    departure_airport_icao=schedule_data['departure_icao'],
                    arrival_airport_icao=schedule_data['arrival_icao'],
                    defaults=schedule_data
                )

            self.stdout.write(self.style.SUCCESS('Flight data for SVO arrivals loaded and updated.'))

        except requests.exceptions.RequestException as e:
            error_message = f"Error fetching flight data: {e}"
            self.stdout.write(self.style.ERROR(error_message))

