from django.db import models
from urllib import request
from django.contrib.auth.models import User
# Create your models here.

class Doctors(models.Model):
    doctor_id = models.SmallIntegerField(primary_key=True)
    Doc_name = models.CharField(max_length=64)
    Current_appointment = models.IntegerField(default=0)
    Total_appointment = models.IntegerField(default=0)

class Patients(models.Model):
    name = models.OneToOneField(User , on_delete=models.CASCADE)
    Pat_name = models.CharField(max_length=64)
    appointment = models.BooleanField(default=False)    
    doctor_id = models.ForeignKey(Doctors, null=True, on_delete=models.CASCADE)
    app_number = models.IntegerField(null=True, blank=True)
