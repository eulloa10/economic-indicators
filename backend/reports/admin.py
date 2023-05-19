from django.contrib import admin
from .models import Subscriber, Report

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
  list_filter = ("user",)
  list_display = ("user", "monthly_subscriber")

class ReportAdmin(admin.ModelAdmin):
  list_filter = ("report_owner", "created_at")
  list_display = ("report_owner", "report_name", "econ_indicator_1", "econ_indicator_1_prior", "econ_indicator_2", "econ_indicator_2_prior", "econ_indicator_3", "econ_indicator_3_prior", "econ_indicator_4", "econ_indicator_4_prior", "econ_indicator_5", "econ_indicator_5_prior", "econ_indicator_6", "econ_indicator_6_prior", "econ_indicator_7", "econ_indicator_7_prior", "econ_indicator_8", "econ_indicator_8_prior", "econ_indicator_9", "econ_indicator_9_prior", "created_at", "updated_at")

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Report, ReportAdmin)
