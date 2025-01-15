from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()

        duration_parts = self.duration.split()
        if len(duration_parts) != 2:
            raise ValidationError("Duration must be in the format '<value> <unit>' (e.g., '1 hour', '2 days').")

        try:
            value = int(duration_parts[0])
        except ValueError:
            raise ValidationError("Duration value must be an integer.")
        
        unit = duration_parts[1].lower()
        valid_units = ['hour', 'day', 'month']
        if unit not in valid_units:
            raise ValidationError(f"Duration unit must be one of {', '.join(valid_units)}.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
