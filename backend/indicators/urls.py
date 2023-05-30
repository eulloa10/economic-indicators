from django.urls import path
from . import views


urlpatterns = [
    path('indicator/<indicator>', views.get_fed_indicator_data, name='indicators')
]
