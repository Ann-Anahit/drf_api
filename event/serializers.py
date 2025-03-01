from rest_framework import serializers
from django.utils import timezone
from event.models import Event

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def validate_event_start(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'The event start cannot be in the past.'
            )
        return value

    def validate_duration(self, value):
        units = ['hour', 'hours', 'day', 'days', 'week', 'weeks']
        if not any(unit in value.lower() for unit in units):
            raise serializers.ValidationError(
                'Duration must be "<number> <unit>", e.g., "3 hours" or "2 days".'
            )
        return value

    def validate_location(self, value):
        if not value:
            raise serializers.ValidationError('Location cannot be empty.')
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Event
        fields = [
           'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'location',
            'event_start', 'duration', 'event_image',
        ]
