from django.db import transaction
from apps.directory.airlines.models.airline import Aircraft, Airline


def relate_airlines_and_aircrafts():
    # Get all unique codeIataAirline values from Aircraft model
    unique_iata_airlines = Aircraft.objects.values_list(
        'codeIataAirline', flat=True).distinct()

    # Create a dictionary to store Airline instances by their codeIataAirline
    airline_dict = {
        airline.codeIataAirline: airline for airline in Airline.objects.all()}

    # Use a transaction to ensure atomicity
    with transaction.atomic():
        for code_iata_airline in unique_iata_airlines:
            # Check if an Airline with the same codeIataAirline exists
            if code_iata_airline in airline_dict:
                airline = airline_dict[code_iata_airline]
                # Update the related Aircraft instances with the Airline
                Aircraft.objects.filter(
                    codeIataAirline=code_iata_airline).update(airline=airline)


# Call the function to relate the models
# relate_airlines_and_aircrafts()
