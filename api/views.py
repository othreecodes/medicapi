from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, views
from rest_framework.decorators import list_route
from rest_framework.response import Response
import requests
from api.forms import FirebaseTokenForm
from api.models import Doctor, DoctorCategory, HealthTip, DoctorRecommendation
from . import serializers
# from .forms import BotProcessingForm
# from api.mixins import BotMixin
from api.mixins import BotMixin
import requests

class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['POST'], url_path="save-token")
    def save_token(self, request, *args, **kwargs):
        form = FirebaseTokenForm(request.data)

        if form.is_valid():
            return Response(form.save())

        return Response(status=400, data=form.errors)



class DoctorViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorCategoryViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorCategorySerializer
    queryset = DoctorCategory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return Response(
            serializers.DoctorSerializer(
                self.get_object().doctor_set.all(), many=True).data)


class HealthTipViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HealthTipSerializer
    queryset = HealthTip.objects.all()


class DoctorRecommendationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorRecommendationSerializer
    queryset = DoctorRecommendation.objects.all()


class BotView(views.APIView, BotMixin):
    def post(self, request):
        data = request.data

        query = data.get("query")

        if query == "diagnose":
            return Response(self.fetch_data_from_grits(data.get('content')))

    @list_route(methods=['POST'], url_path="poll")
    def poll(self, request, *args, **kwargs):

        response = requests.get(
            "http://www.healthmap.org/HMapi.php?auth=956348929582245025&striphtml=1"
        )

        nig = [f for f in response.json() if f['country'] == "Nigeria"]

        return Response(nig)


    