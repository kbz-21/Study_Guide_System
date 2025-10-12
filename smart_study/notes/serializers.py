from rest_framework import serializers
from .models import Note

# Converts Note model to JSON for API
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'is_archived']