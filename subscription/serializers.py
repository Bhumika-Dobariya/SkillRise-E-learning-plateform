from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'student', 'course', 'subscription_type', 'start_date', 'end_date', 'is_active', 'amount']
