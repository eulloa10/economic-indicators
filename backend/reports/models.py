from django.db import models
from django.contrib.auth.models import User
from indicators.models import Indicator

# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_subscriber = models.BooleanField(default=False)

    class Meta:
        db_table="subscribers"

class Report(models.Model):
    report_owner = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=None)
    econ_indicator_1 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_1")
    econ_indicator_1_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_1_prior")
    econ_indicator_2 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_2")
    econ_indicator_2_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_2_prior")
    econ_indicator_3 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_3")
    econ_indicator_3_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_3_prior")
    econ_indicator_4 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_4")
    econ_indicator_4_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_4_prior")
    econ_indicator_5 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_5")
    econ_indicator_5_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_5_prior")
    econ_indicator_6 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_6")
    econ_indicator_6_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_6_prior")
    econ_indicator_7 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_7")
    econ_indicator_7_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_7_prior")
    econ_indicator_8 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_8")
    econ_indicator_8_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_8_prior")
    econ_indicator_9 = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_9")
    econ_indicator_9_prior = models.OneToOneField(Indicator, on_delete=models.CASCADE, related_name="econ_indicator_9_prior")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reports"
