from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="created_groups", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="groups")
    category = models.ForeignKey(Category, related_name="groups", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
