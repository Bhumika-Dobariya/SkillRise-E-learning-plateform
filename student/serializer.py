from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'user', 'email', 'name', 'date_of_birth', 
            'phone_number', 'address', 'gender', 'education', 
            'created_at', 'is_active', 'is_deleted', 'is_verified'
        ]
        extra_kwargs = {
            'email': {'required': False},
            'name': {'required': False},
        }