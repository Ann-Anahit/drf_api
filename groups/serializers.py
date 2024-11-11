from rest_framework import serializers
from .models import Group
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'creator', 'participants',  'category']
