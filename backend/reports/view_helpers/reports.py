import holidays
from datetime import datetime, date, timedelta

daily_indicators = ['yield_curve', 'fed_funds_rate']

def first_business_day(period, isPrior=False):
    us_holidays = holidays.US()
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(period, date_format)

    if isPrior == True:
      date_obj = date_obj - timedelta(days=28)

    day_num = date_obj.strftime("%d")
    first_business_day_of_month = date_obj - timedelta(days=int(day_num) - 1)

    is_holiday = first_business_day_of_month in us_holidays
    is_weekend = first_business_day_of_month.weekday() > 4

    while is_holiday == True or is_weekend == True:
      first_business_day_of_month += datetime.timedelta(days = 1)

    return first_business_day_of_month.strftime("%Y-%m-%d")

def first_business_day_data(first_business_day, observations):
    first_business_day_value = 0

    for data_points in observations:
      if data_points["date"] == first_business_day:
        first_business_day_value = data_points["value"]

    return first_business_day_value

def extract_recent_and_prior_data(indicator, observations):
    recent_and_prior_observations = {}

    recent_period_date = observations[0]['date']
    recent_period_data_point = observations[0]['value']
    prior_period_date = observations[1]['date']
    prior_period_data_point = observations[1]['value']

    if indicator in daily_indicators:
      recent_period_date = first_business_day(recent_period_date)
      recent_period_data_point = first_business_day_data(recent_period_date, observations)
      prior_period_date = first_business_day(prior_period_date, True)
      prior_period_data_point = first_business_day_data(prior_period_date, observations)

    recent_and_prior_observations[recent_period_date] = recent_period_data_point
    recent_and_prior_observations[prior_period_date] = prior_period_data_point
    return recent_and_prior_observations
