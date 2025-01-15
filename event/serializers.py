from rest_framework import serializers
from django.utils import timezone
from events.models import Event

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
        # Example: Only allow durations like "3 hours", "2 days", "1 week"
        pattern = r'^\d+\s+(hours?|days?|weeks?)$'
        if not re.match(pattern, value.lower()):
            raise serializers.ValidationError(
                'Duration must be in the format "<number> <unit>", e.g., "3 hours" or "2 days".'
            )
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
