from rest_framework import serializers
from .models import StudentScore,StudentAnswer

class StudentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentScore
        fields = ['id', 'student', 'quiz', 'obtained_marks', 'total_marks']
        
class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['id', 'student', 'question', 'answer', 'obtained_marks']