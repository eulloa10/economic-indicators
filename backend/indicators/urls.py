from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('indicators/<indicator>', views.get_fed_indicator_data, name='indicator'),
    path('indicators', views.get_all_fed_indicator_data, name='all_indicators'),
]
