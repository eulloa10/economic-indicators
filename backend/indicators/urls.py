from django.urls import path
from . import views


urlpatterns = [
    path('indicator/<indicator>', views.get_indicator_data, name='indicators')
]
