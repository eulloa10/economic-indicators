from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
FRED_API_KEY = os.getenv('FRED_API_KEY')
fred_url = 'https://api.stlouisfed.org/fred/series/observations'

# Create your views here.
def get_yield_data(request):
    payload = {
      'series_id': 'DGS10',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_federal_funds_data(request):
    payload = {
      'series_id': 'EFFR',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_case_shiller_data(request):
    payload = {
      'series_id': 'CSUSHPINSA',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_unemployment_data(request):
    payload = {
      'series_id': 'UNRATE',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_cpi_data(request):
    payload = {
      'series_id': 'CPIAUCSL',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_personal_consumption_data(request):
    payload = {
      'series_id': 'PCE',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_jolts_opening_data(request):
    payload = {
      'series_id': 'JTSJOL',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_jolts_hires_data(request):
    payload = {
      'series_id': 'JTSHIR',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_jolts_turnover_data(request):
    payload = {
      'series_id': 'JTSTSR',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_personal_savings_data(request):
    payload = {
      'series_id': 'PSAVERT',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)

def get_consumer_confidence_data(request):
    payload = {
      'series_id': 'CSCICP03USM665S',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get(fred_url, params=payload)
    data = r.json()
    return JsonResponse(data)
