from django.urls import path
from . import views


urlpatterns = [
  path("yield", views.get_yield_data, name="yield"),
  path("ffr", views.get_federal_funds_data, name="fed-funds-rate"),
  path("csnhpi", views.get_case_shiller_data, name="cash-shiller"),
  path("unemployment", views.get_unemployment_data, name="unemployment"),
  path("cpi", views.get_cpi_data, name="cpi"),
  path("pce", views.get_personal_consumption_data, name="personal-consumption"),
  path("jolts/openings", views.get_jolts_opening_data, name="jolts-openings"),
  path("jolts/hires", views.get_jolts_hires_data, name="jolts-hires"),
  path("jolts/turnover", views.get_jolts_turnover_data, name="jolts-turnover"),
  path("psr", views.get_personal_savings_data, name="personal-savings"),
  path("cci", views.get_consumer_confidence_data, name="consumer-confidence"),
]
