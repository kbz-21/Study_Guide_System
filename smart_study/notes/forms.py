from django import forms
from .models import Note

# Form for creating/editing notes in frontend
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']