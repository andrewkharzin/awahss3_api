from django.shortcuts import render
import logging
# Create your views here.
from tablib import Dataset
from import_export.results import RowResult
from .models.airline import Aircraft, Airline
from .admin import AircraftResource
from django.http import JsonResponse

# Configure logging
logger = logging.getLogger(__name__)

import json

def import_aircrafts(request):
    excel_file_path = 'media/aircrafts_imports.xlsx'  # Specify the path to your Excel file

    logger.info("Starting aircraft import process")
    
    dataset = Dataset()
    with open(excel_file_path, 'rb') as excel_file:
        dataset.load(excel_file.read(), format='xlsx')  # Load data into dataset
    logger.info("Excel file loaded into dataset")
    
    # Convert dataset to a list of dictionaries
    dataset_dict = dataset.dict
    print("Imported data (dictionary format):", dataset_dict)  # Print the loaded data in dictionary format
    
    # Convert the dataset_dict to a JSON string
    dataset_json = json.dumps(dataset_dict, indent=2)
    print("Imported data (JSON format):", dataset_json)  # Print the loaded data in JSON format
    
    aircraft_resource = AircraftResource()
    result = aircraft_resource.import_data(dataset, dry_run=False, collect_failed_rows=True)
    
    if result.has_errors():
        logger.error("Import errors encountered")
        errors_list = []
        for row in result.invalid_rows:
            logger.error(f"Row with errors: {row.errors}")
            errors_list.append(row.errors)
        return JsonResponse({'success': False, 'errors': errors_list})
    else:
        logger.info("Aircraft import successful")
        return JsonResponse({'success': True})





def match_aircrafts_to_airlines(request):
    excel_file_path = 'media/aircrafts.xlsx'  # Specify the path to your Excel file
    
    dataset = Dataset()
    with open(excel_file_path, 'rb') as excel_file:
        dataset.load(excel_file.read(), format='xlsx')  # Load data into dataset
    
    aircraft_resource = AircraftResource()
    for row in dataset.dict:
        code_iata_airline = row.get('airline__codeIataAirline')
        if code_iata_airline:
            aircrafts_to_import = [row]
            aircrafts_data = [dict(row, codeIataAirline=code_iata_airline)]
            dataset.dict = aircrafts_data
            result = aircraft_resource.import_data(dataset, dry_run=False, collect_failed_rows=True)
            if result.has_errors():
                print(f"Import errors for {code_iata_airline}: {result.invalid_rows}")

    if result.has_errors():
        return JsonResponse({'success': False, 'errors': result.invalid_rows})
    else:
        return JsonResponse({'success': True})

