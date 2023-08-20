from django.core.management.base import BaseCommand
from apps.schedules.models import Schedule
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Load schedules from API with specified airline IATA'

    def add_arguments(self, parser):
        parser.add_argument('airline_iata', type=str, help='Airline IATA code')

    def handle(self, *args, **options):
        airline_iata = options['airline_iata']
        access_key = '7c8a729991b6fefbfd9e89863279c947'
        api_url = f'https://api.aviationstack.com/v1/flights'
        params = {'access_key': access_key, 'airline_iata': airline_iata}

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()

            for flight_data in data['data']:
                schedule_data = {
                    # ... map flight data to model fields ...
                }
                Schedule.objects.update_or_create(
                flight_number=schedule_data['flight_number'],
                departure_airport_icao=schedule_data['departure_icao'],
                arrival_airport_icao=schedule_data['arrival_icao'],
                **schedule_data
            )

            self.stdout.write(self.style.SUCCESS(f'Schedules loaded for airline {airline_iata}.'))
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching flight data: {e}")
