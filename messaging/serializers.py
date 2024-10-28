from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model
    """
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    is_sender = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_sender(self, obj):
        request = self.context.get('request')
        return request.user == obj.sender if request else False

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'created_at', 'updated_at', 'content', 'is_sender']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value
