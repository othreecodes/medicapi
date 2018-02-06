from django.contrib import admin
from . import models
# Register your models here.

reg = admin.site.register
reg(models.DoctorCategory)
reg(models.Doctor)
reg(models.DoctorRecommendation)
reg(models.HealthTip)
reg(models.FirebaseToken)