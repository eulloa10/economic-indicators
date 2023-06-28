from rest_framework import serializers
from .models import Indicator, IndicatorReference


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ['id', 'indicator_value', 'indicator_date', 'created_at', 'updated_at', 'indicator_reference_id']

class IndicatorReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorReference
        fields = ['id', 'indicator_series_id', 'indicator_full_name', 'indicator_abbr_name', 'indicator_description', 'created_at', 'updated_at']
