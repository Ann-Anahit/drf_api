from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_image = models.ImageField(
        upload_to='images/', default='../default_post_h52xzo', blank=True
    )
    event_date = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    def clean(self):
        super().clean()

        if self.event_date < timezone.now():
            raise ValidationError({
                'event_date': 'The event date cannot be in the past'
            })
