from django.urls import path
from .views import (
    NoteListCreate, NoteDetail, NoteArchive,
    NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView
)

urlpatterns = [
    # API URLs
    path('', NoteListCreate.as_view(), name='api_notes_list'),
    path('<int:pk>/', NoteDetail.as_view(), name='api_notes_detail'),
    path('<int:pk>/archive/', NoteArchive.as_view(), name='api_notes_archive'),
    # Frontend URLs
    path('list/', NoteListView.as_view(), name='notes_list'),
    path('<int:pk>/detail/', NoteDetailView.as_view(), name='notes_detail'),
    path('create/', NoteCreateView.as_view(), name='notes_create'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='notes_update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='notes_delete'),
]