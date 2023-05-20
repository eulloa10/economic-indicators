from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
FRED_API_KEY = os.getenv('FRED_API_KEY')
fred_api_url = 'https://api.stlouisfed.org/fred/series/observations'

indicator_series_ids = {
    'yield_curve': 'DGS10',
    'fed_funds_rate': 'EFFR',
    'case_shiller': 'CSUSHPINSA',
    'unemployment_rate': 'UNRATE',
    'cpi': 'CPIAUCSL',
    'personal_consumption': 'PCE',
    'jolts_opening': 'JTSJOL',
    'jolts_hires': 'JTSHIR',
    'jolts_turnover': 'JTSTSR',
    'personal_savings': 'PSAVERT',
    'consumer_confidence': 'CSCICP03USM665S'
}

# Create your views here.
def get_indicator_data(request, indicator):
    try:
        payload = {
            'series_id': indicator_series_ids[indicator],
            'api_key': FRED_API_KEY,
            'file_type': 'json',
            'observation_start': '2023-01-01',
            'observation_end': '2023-05-19',
            'sort_order': 'desc'
        }

        r = requests.get(fred_api_url, params=payload)
        data = r.json()
        # Going to return most recent entry
        print("RESPONSE", data["observations"][0])
        return JsonResponse(data)
    except:
        return HttpResponseNotFound('Page Not Found')
