from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=126)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    event_start = models.DateTimeField()
    duration = models.CharField(max_length=100, default='0 hours')
    event_image = models.ImageField(
        upload_to='images/', default='../default_xgered.webp', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
