from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DoctorCategory(models.Model):
    name = models.CharField(max_length=256)


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()
    user = models.ForeignKey(blank=True,null=True,to=User,on_delete=models.CASCADE)
    category = models.ForeignKey(blank=True,null=True,to=DoctorCategory,on_delete=models.CASCADE)
    #TODO: What other fields




