from django.db import models

class PostCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
