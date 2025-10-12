from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .serializers import NoteSerializer
from .forms import NoteForm

# API: List and create notes
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only user's notes, filter by is_archived if provided
        is_archived = self.request.query_params.get('is_archived', 'False') == 'True'
        return Note.objects.filter(user=self.request.user, is_archived=is_archived)

    def perform_create(self, serializer):
        # Assign note to current user
        serializer.save(user=self.request.user)

# API: Retrieve, update, delete note
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

# API: Toggle archive status
class NoteArchive(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        note = Note.objects.get(pk=pk, user=request.user)
        note.is_archived = not note.is_archived
        note.save()
        return Response(NoteSerializer(note).data)

# Frontend: List notes
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user, is_archived=False)

# Frontend: View note details
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/detail.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

# Frontend: Create note
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/form.html'
    success_url = reverse_lazy('notes_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Frontend: Update note
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/form.html'
    success_url = reverse_lazy('notes_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

# Frontend: Delete note
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)