from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Indicator
from reports.models import Report
import requests
import os
import json
import ast
from datetime import date, timedelta
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

payload = {
    'api_key': FRED_API_KEY,
    'file_type': 'json',
    'sort_order': 'desc'
}

def standardize_observations(observations):
    all_queried_obs = {}
    for obs in observations:
        date = obs["date"]
        value = obs["value"]
        all_queried_obs[date] = value
    return all_queried_obs

"""
Customer will choose the end date

For daily -> We will get the most recent item in the list (index 0) and then we will loop through and find the last item of the previous month
For monthly -> We will just get the two most recent objects in the list
"""
def get_fed_indicator_data(request, indicator):
    # observation_end = date.fromisoformat(request.GET['observation_end'])
    observation_end = date.today()
    # observation_start = observation_end - timedelta(weeks=24)

    # payload['observation_start'] = observation_start
    payload['observation_end'] = observation_end

    try:
        payload['series_id'] = indicator_series_ids[indicator]
        r = requests.get(fred_api_url, params=payload)
        data = r.json()
        formatted_data = standardize_observations(data['observations'])
        return JsonResponse({
            indicator: formatted_data
        })
    except:
        return HttpResponseNotFound('Page Not Found')


def get_all_fed_indicator_data(request):
    observation_end = date.today()
    observation_start = observation_end - timedelta(weeks=24)
    all_indicator_data = {}

    payload['observation_start'] = observation_start
    payload['observation_end'] = observation_end

    try:
        for indicator in indicator_series_ids.keys():
            payload['series_id'] = indicator_series_ids[indicator]
            r = requests.get(fred_api_url, params=payload)
            data = r.json()
            formatted_data = standardize_observations(data['observations'])
            all_indicator_data[indicator] = formatted_data
        return JsonResponse({
            "indicators": all_indicator_data
        })
    except:
        return HttpResponseNotFound('Page Not Found')
