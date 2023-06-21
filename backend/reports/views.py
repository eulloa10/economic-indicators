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

daily_indicators = ['yield_curve', 'fed_funds_rate']

payload = {
    'api_key': FRED_API_KEY,
    'file_type': 'json',
    'sort_order': 'desc'
}

def extract_recent_and_prior_data(indicator, observations):
    recent_and_prior_observations = {}

    if indicator in daily_indicators:
      recent_period_date

    recent_period_date = observations[0]['date']
    recent_period_data_point = observations[0]['value']
    prior_period_date = observations[1]['date']
    prior_period_data_point = observations[1]['value']
    recent_and_prior_observations[recent_period_date] = recent_period_data_point
    recent_and_prior_observations[prior_period_date] = prior_period_data_point
    print(recent_and_prior_observations)
    return recent_and_prior_observations

def get_recent_indicator_data(request):
    observation_end = date.today()
    observation_start = observation_end - timedelta(weeks=24)
    recent_indicator_data = {}

    payload['observation_start'] = observation_start
    payload['observation_end'] = observation_end

    try:
        for indicator in indicator_series_ids.keys():
            payload['series_id'] = indicator_series_ids[indicator]
            r = requests.get(fred_api_url, params=payload)
            data = r.json()
            recent_indicator_data[indicator] = extract_recent_and_prior_data(indicator, data['observations'])
        return JsonResponse({
            "indicators": recent_indicator_data
        })
    except:
        return HttpResponseNotFound('Page Not Found')
