from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from youtubesearchpython import VideosSearch
from .models import YouTubeSearchHistory
from .serializers import SearchHistorySerializer, SearchRequestSerializer

# API: Perform YouTube search and save history
@method_decorator(csrf_exempt, name='dispatch')
class YouTubeSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SearchRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        query = serializer.validated_data['q']
        try:
            search = VideosSearch(query, limit=10)
            results = search.result()['result']

            # Process results with validation
            videos = []
            for item in results:
                # Skip if critical fields are missing or None
                if not all([item.get('id'), item.get('title'), item.get('channel'), item.get('thumbnails')]):
                    continue
                try:
                    videos.append({
                        'video_id': item['id'],
                        'title': item['title'],
                        'channel': item['channel'].get('name', 'Unknown Channel'),
                        'thumbnail': item['thumbnails'][0]['url'] if item['thumbnails'] else '',
                        'published_at': item.get('publishedTime', 'Unknown'),
                        'url': f"https://www.youtube.com/watch?v={item['id']}"
                    })
                except (KeyError, TypeError, IndexError):
                    continue  # Skip malformed entries

            # Save to history
            YouTubeSearchHistory.objects.create(user=request.user, query=query)

            return Response({
                'query': query,
                'videos': videos,
                'total_results': len(videos),
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Search failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API: List search history
@method_decorator(csrf_exempt, name='dispatch')
class SearchHistoryView(generics.ListAPIView):
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return YouTubeSearchHistory.objects.filter(user=self.request.user).order_by('-created_at')