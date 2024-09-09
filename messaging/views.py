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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receiver']

    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        if user_id:
            return self.queryset.filter(receiver_id=user_id)
        return self.queryset

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
