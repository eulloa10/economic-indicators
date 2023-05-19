from django.contrib import admin
from .models import IndicatorReference, Indicator

# Register your models here.

class IndicatorReferenceAdmin(admin.ModelAdmin):
  list_filter = ("indicator_name",)
  list_display = ("indicator_abbr_name", "indicator_name", "indicator_series_id", "indicator_description", "created_at", "updated_at")

class IndicatorAdmin(admin.ModelAdmin):
  list_filter = ("indicator_date",)
  list_display = ("indicator_value", "indicator_date", "indicator_reference", "created_at", "updated_at")

admin.site.register(IndicatorReference, IndicatorReferenceAdmin)
admin.site.register(Indicator, IndicatorAdmin)
