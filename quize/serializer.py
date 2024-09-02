from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            'id', 'title', 'description', 'total_marks', 'duration', 
            'passing_marks', 'instructor', 'module', 'is_active', 
            'is_published', 'created_at', 'updated_at'
        ]