from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password') + ('is_staff','is_active','date_joined')
        read_only_fields = ('is_staff','is_active','date_joined')