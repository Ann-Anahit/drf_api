from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        # Check if the user is authenticated before setting sender
        if self.request.user.is_authenticated:
            serializer.save(sender=self.request.user)
        else:
            serializer.save()  # Saves without sender if user is anonymous

    def get_queryset(self):
        # Show all messages for unauthenticated users
        if self.request.user.is_authenticated:
            user = self.request.user
            user_id = self.request.query_params.get('user')
            if user_id:
                return self.queryset.filter(receiver_id=user_id, sender=user)
            return self.queryset.filter(sender=user) | self.queryset.filter(receiver=user)
        return self.queryset  # Return all messages for unauthenticated users


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
            raise permissions.PermissionDenied("You can only edit your own messages.")
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
        return Message.objects.filter(
            models.Q(sender=sender, receiver_id=receiver_id) |
            models.Q(sender_id=receiver_id, receiver=sender)
        ).order_by('created_at')
