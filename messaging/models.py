from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Message model, related to User
    """
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}: {self.content[:20]}"
