from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            'id',
            'course',
            'title',
            'description',
            'chapter',
            'content',
            'video_url',
            'quiz_url',
            'assignment_url',
            'is_published',
            'created_at',
            'updated_at'
        ]