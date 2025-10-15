from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import ToDo
from .serializers import ToDoSerializer

# API: List and create to-dos
@method_decorator(csrf_exempt, name='dispatch')
class ToDoListCreate(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only user's to-dos, filter by is_completed if provided
        is_completed = self.request.query_params.get('is_completed', 'False') == 'True'
        return ToDo.objects.filter(user=self.request.user, is_completed=is_completed)

    def perform_create(self, serializer):
        # Assign to-do to current user
        serializer.save(user=self.request.user)

# API: Retrieve, update, delete to-do
@method_decorator(csrf_exempt, name='dispatch')
class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

# API: Toggle complete status
@method_decorator(csrf_exempt, name='dispatch')
class ToDoComplete(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        todo = ToDo.objects.get(pk=pk, user=request.user)
        todo.is_completed = not todo.is_completed
        todo.save()
        return Response(ToDoSerializer(todo).data)