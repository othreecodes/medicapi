from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    