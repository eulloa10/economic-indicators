from django.db import models

# Create your models here.
class IndicatorReference(models.Model):
    indicator_series_id = models.CharField(max_length=None, unique=True)
    indicator_full_name = models.CharField(max_length=None, unique=True)
    indicator_abbr_name = models.CharField(max_length=None, unique=True)
    indicator_description = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "indicator_references"

class Indicator(models.Model):
    indicator_value = models.DecimalField(max_digits=10, decimal_places=2)
    indicator_date = models.DateField()
    indicator_reference = models.ForeignKey(IndicatorReference, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "indicators"
