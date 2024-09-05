from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['phone_number', 'message']

    def validate_phone_number(self, value):
        if len(value) != 13 or not value.startswith('+') or not value[1:].isdigit():
            raise serializers.ValidationError('Phone number must be in the format +91XXXXXXXXXX and exactly 13 characters long.')
        return value
