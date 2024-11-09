from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        # Ensure the user is authenticated
        if not self.request.user.is_authenticated:
            return Message.objects.none()  # Return an empty queryset if user is not authenticated

        recipient = self.request.query_params.get('recipient', None)
        if recipient:
            return Message.objects.filter(recipient__username=recipient).order_by('timestamp')

        # Return messages sent/received by the current user
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(recipient=self.request.user)

    @action(detail=False, methods=['post'])
    def send(self, request):
        """
        Endpoint to send a message.
        """
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
        return Response(self.get_serializer(message).data, status=201)
