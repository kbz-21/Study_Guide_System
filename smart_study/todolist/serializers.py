from rest_framework import serializers
from .models import ToDo

# Converts ToDo model to JSON for API
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']