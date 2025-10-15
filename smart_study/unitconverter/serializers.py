from rest_framework import serializers
from .models import Conversion

# Serializer for conversion history
class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = ['id', 'value', 'from_unit', 'to_unit', 'result', 'created_at']

# Serializer for conversion request
class ConversionRequestSerializer(serializers.Serializer):
    value = serializers.FloatField()
    from_unit = serializers.ChoiceField(choices=['yard', 'foot', 'pound', 'kilogram'])
    to_unit = serializers.ChoiceField(choices=['yard', 'foot', 'pound', 'kilogram'])