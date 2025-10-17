from django.urls import path
from .views import YouTubeSearchView, SearchHistoryView

urlpatterns = [
    path('search/', YouTubeSearchView.as_view(), name='api_youtube_search'),
    path('history/', SearchHistoryView.as_view(), name='api_search_history'),
    
]