from django.db import models

# Create your models here.
class IndicatorReference(models.Model):
    indicator_series_id = models.CharField(max_length=None, blank=False)
    indicator_name = models.CharField(max_length=None)
    indicator_description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
      db_table = "indicator_references"

class Indicator(models.Model):
    # indicator_reference_id as FK
    indicator_value = models.DecimalField(max_digits=10, decimal_places=2)
    indicator_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
