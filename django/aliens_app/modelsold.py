from django.db import models
from django.db import connection

# Create your models here.

class GovernmentEmployee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    country = models.CharField(max_length=25)
    position = models.CharField(max_length=35)