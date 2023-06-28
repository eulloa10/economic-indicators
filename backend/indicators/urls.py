from django.urls import path, include
from rest_framework import routers
from .views import indicator_data, indicator_reference_data

urlpatterns = [
    path('indicators/reference', indicator_reference_data, name='indicator_reference'),
    path('indicators/<str:indicator>', indicator_data, name='indicator'),

]

# urlpatterns = [
#     path('indicators/<indicator>', views.get_fed_indicator_data, name='indicator'),
#     path('indicators', views.get_all_fed_indicator_data, name='all_indicators'),
# ]
