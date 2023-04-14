from django.urls import path
from . import views


urlpatterns = [
  path("indicator/yield", views.get_yield_data, name="yield"),
  path("indicator/ffr", views.get_federal_funds_data, name="fed-funds-rate"),
  path("indicator/csnhpi", views.get_case_shiller_data, name="cash-shiller"),
  path("indicator/unemployment", views.get_unemployment_data, name="unemployment"),
  path("indicator/cpi", views.get_cpi_data, name="cpi"),
  path("indicator/pce", views.get_personal_consumption_data, name="personal-consumption"),
  path("indicator/jolts/openings", views.get_jolts_opening_data, name="jolts-openings"),
  path("indicator/jolts/hires", views.get_jolts_hires_data, name="jolts-hires"),
  path("indicator/jolts/turnover", views.get_jolts_turnover_data, name="jolts-turnover"),
  path("indicator/psr", views.get_personal_savings_data, name="personal-savings"),
  path("indicator/cci", views.get_consumer_confidence_data, name="consumer-confidence"),
]
