from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    
    created_at = serializers.DateTimeField(source='timestamp', format='%Y-%m-%dT%H:%M:%SZ')


    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'created_at']

