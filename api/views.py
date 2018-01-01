from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from api.models import Doctor, DoctorCategory
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

class DoctorViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorCategoryViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorCategorySerializer
    queryset = DoctorCategory.objects.all()
