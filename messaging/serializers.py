from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile 
from .models import Message

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'bio']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'text', 'timestamp']
