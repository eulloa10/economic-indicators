from rest_framework import serializers
import models


class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Indicator
        fields = ['url', 'id', 'indicator_value', 'indicator_date', 'created_at', 'updated_at', 'indicator_reference_id']

class IndicatorReferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndicatorReference
        fields = ['url', 'id', 'indicator_series_id', 'indicator_full_name', 'indicator_abbr_name', 'indicator_description', 'created_at', 'updated_at']
