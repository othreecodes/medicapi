from django.contrib import admin
from . import models
from . import forms

# Register your models here.

reg = admin.site.register
reg(models.DoctorCategory)
reg(models.Doctor)
reg(models.DoctorRecommendation)


@admin.register(models.HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = forms.HealthTipFrom


# reg(models.HealthTip)
reg(models.FirebaseToken)
