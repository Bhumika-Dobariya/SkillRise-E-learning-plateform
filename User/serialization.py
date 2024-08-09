from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib import admin
from .models import OTP
from uuid import UUID


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_type', 'email', 'name', 'password', 'date_of_birth', 'phone_number', 'address', 'gender', 'education', 'is_active', 'is_deleted', 'is_verified', 'last_login']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}, 
            'last_login': {'read_only': True},
        }
      
      
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'




class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class OTPVerificationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)