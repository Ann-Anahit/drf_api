from django.db import models
from django.contrib.auth.models import User

# Profile model to represent user information (e.g., avatar, bio)
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messaging_profile')  # Add related_name
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Message model to store conversation messages
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username}"
    
    class Meta:
        ordering = ['timestamp']
