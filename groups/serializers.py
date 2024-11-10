from rest_framework import serializers
from .models import Group, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class GroupSerializer(serializers.ModelSerializer):
    category = CategorySerializer() 

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'creator', 'members', 'category']
