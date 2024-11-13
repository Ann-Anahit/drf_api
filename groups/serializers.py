from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Group, Category

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'creator', 'category', 'participants']  # Explicitly exclude timestamps

    def validate_category(self, value):
        """Ensure the category exists for the provided ID."""
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Invalid category ID.")
        return value

    def create(self, validated_data):
        # Ensure category is set in the data
        category_id = validated_data.get('category')
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            validated_data['category'] = category
        
        # Create the group without including 'created_at' or 'updated_at'
        group = Group.objects.create(**validated_data)

        # Optionally add the creator as a participant if they aren't already
        group.participants.add(self.context['request'].user)
        return group

    def update(self, instance, validated_data):
        category_id = validated_data.get('category')
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            validated_data['category'] = category
        
        # Update the group with the new validated data, excluding 'created_at' and 'updated_at'
        for attr, value in validated_data.items():
            if attr not in ['created_at', 'updated_at']:  # Skip the timestamps
                setattr(instance, attr, value)
        instance.save()
        return instance
