from rest_framework import serializers
from django.utils import timezone
from event.models import Event
import re


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
                'Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!')
        return value

    def validate_event_start(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'The event start cannot be in the past.'
            )
        return value

    def validate_duration(self, value):
        """
        Validates that the duration is in the format 
        '<positive integer> <unit>'
        and the unit is one of the allowed units.
        """
        allowed_units = ['hour', 'hours', 'day', 'days', 'week', 'weeks']
        duration_pattern = r'^\s*(\d+)\s+([a-zA-Z]+)\s*$' 

        match = re.match(duration_pattern, value)
        if not match:
            raise serializers.ValidationError(
                'Duration must be in the format "<positive integer> <unit>" '
                '(e.g., "1 hour", "2 days"). Valid units are: hour, hours, day, days, week, weeks.'
            )

        number, unit = match.groups()
        if int(number) < 1 or unit.lower() not in allowed_units:
            raise serializers.ValidationError(
               f'Enter a positive number with a valid unit: {", ".join(allowed_units)}.'
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
