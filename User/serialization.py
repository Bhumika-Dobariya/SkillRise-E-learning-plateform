from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib import admin
from .models import OTP
from uuid import UUID



        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'role', 'is_active', 'is_deleted', 'is_verified', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
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