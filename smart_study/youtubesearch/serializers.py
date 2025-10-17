from rest_framework import serializers
from .models import YouTubeSearchHistory

# Serializer for search history
class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeSearchHistory
        fields = ['id', 'query', 'created_at']

# Serializer for search request
class SearchRequestSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=255)