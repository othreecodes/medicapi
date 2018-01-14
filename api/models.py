from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class DoctorCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()
    user = models.ForeignKey(blank=True, null=True, to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(blank=True, null=True, to=DoctorCategory, on_delete=models.CASCADE)

    # TODO: What other fields

    def __str__(self):
        return self.name


class HealthTip(TimeStampedModel):
    title = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()

    def __str__(self):
        return self.slug


class FirebaseToken(models.Model):
    token = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=256,verbose_name="Firebase Messaging Token",blank=True,null=True)

    def __str__(self):
        return self.user.username

class DoctorRecommendation(TimeStampedModel):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title