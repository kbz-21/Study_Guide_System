from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Conversion
from .serializers import ConversionSerializer, ConversionRequestSerializer

# Conversion logic
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Length conversions
    if from_unit == 'yard' and to_unit == 'foot':
        return value * 3
    if from_unit == 'foot' and to_unit == 'yard':
        return value / 3
    # Mass conversions
    if from_unit == 'pound' and to_unit == 'kilogram':
        return value * 0.453592
    if from_unit == 'kilogram' and to_unit == 'pound':
        return value * 2.20462
    raise ValueError("Invalid unit conversion")

# API: Perform conversion and save history
@method_decorator(csrf_exempt, name='dispatch')
class ConvertView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ConversionRequestSerializer(data=request.data)
        if serializer.is_valid():
            value = serializer.validated_data['value']
            from_unit = serializer.validated_data['from_unit']
            to_unit = serializer.validated_data['to_unit']
            try:
                result = convert_units(value, from_unit, to_unit)
                conversion = Conversion.objects.create(
                    user=request.user,
                    value=value,
                    from_unit=from_unit,
                    to_unit=to_unit,
                    result=result
                )
                return Response(ConversionSerializer(conversion).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API: List conversion history
@method_decorator(csrf_exempt, name='dispatch')
class ConversionHistory(generics.ListAPIView):
    serializer_class = ConversionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversion.objects.filter(user=self.request.user)

# API: Retrieve specific conversion
@method_decorator(csrf_exempt, name='dispatch')
class ConversionDetail(generics.RetrieveAPIView):
    serializer_class = ConversionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversion.objects.filter(user=self.request.user)