from rest_framework import serializers
from .models import Notification
from student.models import Student


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','recipient', 'notification_type', 'message']