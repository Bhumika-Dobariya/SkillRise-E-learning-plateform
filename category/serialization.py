from rest_framework import serializers
from .models import Category


class categoryserialization(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
       