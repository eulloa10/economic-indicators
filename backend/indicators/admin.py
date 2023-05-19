from django.contrib import admin
from .models import IndicatorReference, Indicator

# Register your models here.

class IndicatorReferenceAdmin(admin.ModelAdmin):
  list_filter = ("indicator_name",)
  list_display = ("indicator_name", "indicator_value", "indicator_description", "indicator_date")

class IndicatorAdmin(admin.ModelAdmin):
  list_filter = ("indicator_date",)
  list_display = ("indicator_value", "indicator_date", "indicator_reference", "created_at", "updated_at")

admin.site.register(IndicatorReference, IndicatorReferenceAdmin)
admin.site.register(Indicator, IndicatorAdmin)
