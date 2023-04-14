from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
FRED_API_KEY = os.getenv('FRED_API_KEY')

# Create your views here.
def get_yield_data(request):
    payload = {
      'series_id': 'DGS10',
      'api_key': FRED_API_KEY,
      'file_type': 'json',
      'observation_start': '2023-04-01'
    }

    r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
    data = r.json()
    return JsonResponse(data)

def get_federal_funds_data(request):
    return HttpResponse("fed funds")

def get_case_shiller_data(request):
    return HttpResponse("case shiller")

def get_unemployment_data(request):
    return HttpResponse("unemployment")

def get_cpi_data(request):
    return HttpResponse("cpi")

def get_personal_consumption_data(request):
    return HttpResponse("personal consumption")

def get_jolts_opening_data(request):
    return HttpResponse("jolts opening")

def get_jolts_hires_data(request):
    return HttpResponse("jolts hires")

def get_jolts_turnover_data(request):
    return HttpResponse("jolts turnovers")

def get_personal_savings_data(request):
    return HttpResponse("personal savings")

def get_consumer_confidence_data(request):
    return HttpResponse("consumer confidence")
