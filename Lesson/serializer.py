
from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'content',
            'module',
            'chapter',
            'duration',
            'resources',
            'video_url',
            'created_at',
            'updated_at',
            'is_active',
            'is_deleted',
        ]