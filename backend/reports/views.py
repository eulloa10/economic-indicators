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

def first_business_day(recent_period):
    us_holidays = holidays.US()
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(recent_period, date_format)
    day_num = date_obj.strftime("%d")
    first_business_day_of_month = date_obj - timedelta(days=int(day_num) - 1)

    is_holiday = first_business_day_of_month in us_holidays
    is_weekend = first_business_day_of_month.weekday() > 4

    while is_holiday == True or is_weekend == True:
      first_business_day_of_month += datetime.timedelta(days = 1)

    return first_business_day_of_month

def extract_recent_and_prior_data(indicator, observations):
    recent_and_prior_observations = {}

    recent_period_date = observations[0]['date']
    recent_period_data_point = observations[0]['value']
    prior_period_date = observations[1]['date']
    prior_period_data_point = observations[1]['value']

    if indicator in daily_indicators:
      recent_period_date = first_business_day(recent_period_date).strftime("%m/%d/%Y")
      print("RPD: ", recent_period_date)

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
