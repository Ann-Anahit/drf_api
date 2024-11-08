from rest_framework import viewsets
from rest_framework import permissions
from .models import Message, Profile
from .serializers import MessageSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def current_user(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        recipient = self.request.query_params.get('recipient', None)
        if recipient:
            return Message.objects.filter(recipient_id=recipient).order_by('timestamp')
        return Message.objects.none()

    @action(detail=False, methods=['post'])
    def send(self, request):
        sender = request.user
        recipient_id = request.data.get('recipient')
        text = request.data.get('text')

        if not recipient_id or not text:
            return Response({'detail': 'Recipient and text are required.'}, status=400)

        recipient = User.objects.get(id=recipient_id)

        message = Message.objects.create(sender=sender, recipient=recipient, text=text)
        return Response(self.get_serializer(message).data)
