from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class DoctorCategory(models.Model):
    name = models.CharField(max_length=256)

    # objects = models.Manager()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()
    user = models.OneToOneField(
        blank=True, null=True, to=User, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        blank=True, null=True, to=DoctorCategory, on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True, null=True, default="default.jpg")

    # TODO: What other fields
    # objects = models.Manager()

    def __str__(self):
        return self.name


class HealthTip(TimeStampedModel):
    title = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, default="default.jpg")

    def __str__(self):
        return self.slug


class FirebaseToken(models.Model):
    token = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fcm_token = models.CharField(
        max_length=256,
        verbose_name="Firebase Messaging Token",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.first_name


class DoctorRecommendation(TimeStampedModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Consultaion(models.Model):
    pass
