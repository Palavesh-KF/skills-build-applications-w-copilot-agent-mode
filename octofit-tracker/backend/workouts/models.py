from django.db import models
from django.contrib.auth.models import User

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion for {self.user.username} at {self.created_at}"
