from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Indicator
from reports.models import Report
import requests
import os
import json
import ast
import holidays
from datetime import datetime, date, timedelta
from dotenv import load_dotenv, find_dotenv
from .view_helpers.reports import  extract_recent_and_prior_data, first_business_day, first_business_day_data


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
