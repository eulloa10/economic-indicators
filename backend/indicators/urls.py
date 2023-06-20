from django.urls import path
from . import views


urlpatterns = [
    path('indicator/<indicator>', views.get_fed_indicator_data, name='indicator'),
    path('indicators', views.get_all_fed_indicator_data, name='all_indicators'),
    path('reports/latest', views.get_recent_indicator_data, name='recent_indicators')
]
