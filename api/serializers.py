from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Doctor, DoctorCategory, HealthTip


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'token') + (
        'is_staff', 'is_active', 'date_joined')
        read_only_fields = ('is_staff', 'is_active', 'date_joined')

    def get_token(self, obj):
        try:
            return obj.firebasetoken.token
        except ObjectDoesNotExist as e:
            return None


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorCategory
        fields = "__all__"


class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = "__all__"
        read_only_fields = ('created', 'modified')
