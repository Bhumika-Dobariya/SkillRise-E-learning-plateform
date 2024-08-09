from rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'id', 
            'name', 
            'email', 
            'phone_number', 
            'department', 
            'qualification', 
            'experience', 
            'course_name', 
            'date_of_joining', 
            'is_active', 
            'address', 
            'gender', 
            'created_at', 
            'updated_at'
        ]
        