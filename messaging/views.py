from rest_framework import viewsets
from rest_framework import permissions
from profiles.models import Profile
from .models import Message
from .serializers import MessageSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def current_user(self, request):
        try:
            # Fetch the profile for the authenticated user
            profile = Profile.objects.get(owner=request.user)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found for the current user.")
        
        # Serialize and return the profile data
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch messages based on the recipient query parameter or all messages for the user
        recipient = self.request.query_params.get('recipient', None)
        if recipient:
            return Message.objects.filter(recipient_id=recipient).order_by('timestamp')
        
        # If no recipient provided, return messages for the current user (both sent and received)
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(recipient=self.request.user)

    @action(detail=False, methods=['post'])
    def send(self, request):
        sender = request.user
        recipient_id = request.data.get('recipient')
        text = request.data.get('text')

        # Validate input
        if not recipient_id or not text:
            return Response({'detail': 'Recipient and text are required.'}, status=400)

        try:
            recipient = User.objects.get(id=recipient_id)
        except User.DoesNotExist:
            return Response({'detail': 'Recipient not found.'}, status=404)

        # Create and save the new message
        message = Message.objects.create(sender=sender, recipient=recipient, text=text)
        return Response(self.get_serializer(message).data)
