import os
import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from dotenv import load_dotenv
from .models import YouTubeSearchHistory
from .serializers import SearchHistorySerializer, SearchRequestSerializer

load_dotenv()

# YouTube API endpoint
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
API_KEY = os.getenv('YOUTUBE_API_KEY')

# API: Perform YouTube search and save history
@method_decorator(csrf_exempt, name='dispatch')
class YouTubeSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SearchRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if not API_KEY:
            return Response({'error': 'YouTube API key not configured.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        query = serializer.validated_data['q']
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': 10,
            'order': 'relevance',
            'key': API_KEY,
        }

        try:
            response = requests.get(YOUTUBE_API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Process results
            videos = []
            for item in data.get('items', []):
                snippet = item['snippet']
                video_id = item['id']['videoId']
                videos.append({
                    'video_id': video_id,
                    'title': snippet['title'],
                    'channel': snippet['channelTitle'],
                    'thumbnail': snippet['thumbnails']['default']['url'],
                    'published_at': snippet['publishedAt'],
                    'url': f'https://www.youtube.com/watch?v={video_id}',
                })

            # Save to history
            YouTubeSearchHistory.objects.create(user=request.user, query=query)

            return Response({
                'query': query,
                'videos': videos,
                'total_results': data.get('pageInfo', {}).get('totalResults', 0),
            }, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({'error': f'API request failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API: List search history
@method_decorator(csrf_exempt, name='dispatch')
class SearchHistoryView(generics.ListAPIView):
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return YouTubeSearchHistory.objects.filter(user=self.request.user).order_by('-created_at')