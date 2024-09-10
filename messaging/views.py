from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import MessageSerializer
from drf_api.permissions import IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        # Ensure the sender is set to the currently authenticated user
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        # Filter messages where the authenticated user is the sender or receiver
        user = self.request.user
        user_id = self.request.query_params.get('user')  # Optional filter for specific receiver
        if user_id:
            return self.queryset.filter(receiver_id=user_id, sender=user)
        # If no 'user' parameter, return all messages where the authenticated user is the sender or receiver
        return self.queryset.filter(sender=user) | self.queryset.filter(receiver=user)

class MessageDetail(generics.RetrieveAPIView):
    """
    Retrieve a message by its id.
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class MessageUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a message if you're the sender.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Message.objects.all()

    def perform_update(self, serializer):
        if self.request.user != self.get_object().sender:
            raise PermissionDenied("You can only edit your own messages.")
        serializer.save()

class ConversationList(generics.ListAPIView):
    """
    List all messages exchanged between two users (sender and receiver).
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        sender = self.request.user
        receiver_id = self.kwargs['receiver_id']
        logger.info(f'Fetching conversation between sender: {sender} and receiver_id: {receiver_id}')
        return Message.objects.filter(
            models.Q(sender=sender, receiver_id=receiver_id) |
            models.Q(sender_id=receiver_id, receiver=sender)
        ).order_by('created_at')
