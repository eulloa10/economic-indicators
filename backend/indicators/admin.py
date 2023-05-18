from django.contrib import admin
from .models import IndicatorReference

# Register your models here.

class IndicatorReferenceAdmin(admin.ModelAdmin):
  list_filter = ("indicator_name", )
  list_display = ("indicator_name", "indicator_value", "indicator_description", "indicator_date")

admin.site.register(IndicatorReference, IndicatorReferenceAdmin)
