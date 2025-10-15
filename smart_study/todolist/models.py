from django.db import models
from users.models import CustomUser

# Model for to-dos, linked to user
class ToDo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title