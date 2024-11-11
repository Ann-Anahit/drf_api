from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Group, Category
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def perform_create(self, serializer):
        # Retrieve the category id (which is the pk) from the request data
        category_id = self.request.data.get("category")
        
        # Check if category_id is present in the request
        if not category_id:
            raise ValueError("Category ID is required")

        # Get the Category object using the primary key (category_id)
        category = get_object_or_404(Category, pk=category_id)

        # Save the new group with the creator and the category
        serializer.save(creator=self.request.user, category=category)
        
        # Add the creator as the first participant
        group = serializer.instance
        group.participants.add(self.request.user)
