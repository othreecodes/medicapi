from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Doctor, DoctorCategory, HealthTip,DoctorRecommendation


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'token') + (
        'is_staff', 'is_active', 'date_joined')
        read_only_fields = ('is_staff', 'is_active', 'date_joined')
        

    def get_token(self, obj):
        try:
            return obj.firebasetoken.token
        except ObjectDoesNotExist as e:
            return None


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 1

class DoctorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorCategory
        fields = "__all__"


class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = "__all__"
        read_only_fields = ('created', 'modified')


class DoctorRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRecommendation
        fields = "__all__"
        read_only_fields = ('created', 'modified')
        