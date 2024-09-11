from django.db import models  
from django.db.models.signals import post_save  
from django.contrib.auth.models import User  

class Profile(models.Model):  
    owner = models.OneToOneField(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    name = models.CharField(max_length=255, blank=True)  
    content = models.TextField(blank=True)  
    image = models.ImageField(upload_to='images/', default='../default_profile_image.png')  # Ensure this path is correct  

    class Meta:  
        ordering = ['-created_at']  

    def __str__(self):  
        return f"{self.owner}'s profile"  

def create_profile(sender, instance, created, **kwargs):  
    if created:  
        Profile.objects.create(owner=instance)  

# Connect the signal to the User model  
post_save.connect(create_profile, sender=User)  

class Message(models.Model):  
    profile = models.ForeignKey(Profile, related_name='messages', on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"Message from {self.profile.owner.username}: {self.content[:20]}"