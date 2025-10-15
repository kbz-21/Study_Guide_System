from django.db import models
from users.models import CustomUser

# Model to store conversion history
class Conversion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='conversions')
    value = models.FloatField()
    from_unit = models.CharField(max_length=50)
    to_unit = models.CharField(max_length=50)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} {self.from_unit} to {self.to_unit} = {self.result}"