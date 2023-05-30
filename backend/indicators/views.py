from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
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

def standardize_observations(observations):
    all_queried_obs = {}
    for obs in observations:
        date = obs["date"]
        value = obs["value"]
        all_queried_obs[date] = value
    return all_queried_obs

def get_indicator_data(request, indicator):
    observation_end = date.fromisoformat(request.GET['observation_end'])
    observation_start = observation_end - timedelta(weeks=24)

    payload = {
        'api_key': FRED_API_KEY,
        'file_type': 'json',
        'observation_start': observation_start,
        'observation_end': observation_end,
        'sort_order': 'desc'
    }
    """
    Customer will choose the end date

    For daily -> We will get the most recent item in the list (index 0) and then we will loop through and find the last item of the previous month
    For monthly -> We will just get the two most recent objects in the list
    """
    try:
        payload['series_id'] = indicator_series_ids[indicator]
        r = requests.get(fred_api_url, params=payload)
        data = r.json()
        # Going to return most recent entry
        # print("RESPONSE", data["observations"][0])
        formatted_data = standardize_observations(data['observations'])
        return JsonResponse({
            indicator: formatted_data
        })
    except:
        return HttpResponseNotFound('Page Not Found')
