from django.urls import path
from . import views


urlpatterns = [
    path('reports/latest', views.get_recent_indicator_data, name='recent_indicators')
]
