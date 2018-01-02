from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.forms import FirebaseTokenForm
from api.models import Doctor, DoctorCategory, HealthTip
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['POST'], url_path="save-token")
    def save_token(self, request, *args, **kwargs):
        form = FirebaseTokenForm(request.data)

        if form.is_valid():
            return Response(form.save())

        return Response(form.errors)


class DoctorViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorCategoryViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorCategorySerializer
    queryset = DoctorCategory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return Response(serializers.DoctorSerializer(self.get_object().doctor_set.all(), many=True).data)


class HealthTipViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HealthTipSerializer
    queryset = HealthTip.objects.all()
