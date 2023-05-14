from django.db import models

# Create your models here.
class Indicators(models.Model):
  id = models.AutoField(primary_key=True)
  indicator_name = models.CharField(max_length=None)
  indicator_value = models.DecimalField(max_digits=10, decimal_places=2)
  indicator_description = models.TextField()
  indicator_date = models.DateField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)
