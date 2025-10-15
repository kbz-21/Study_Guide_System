from django.urls import path
from .views import ConvertView, ConversionHistory, ConversionDetail

urlpatterns = [
    path('convert/', ConvertView.as_view(), name='api_convert'),
    path('history/', ConversionHistory.as_view(), name='api_conversion_history'),
    path('history/<int:pk>/', ConversionDetail.as_view(), name='api_conversion_detail'),
]