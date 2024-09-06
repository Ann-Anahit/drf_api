from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import MessageSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class MessageListCreate(generics.ListCreateAPIView):
    """
    List messages or create a new message if logged in.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receiver']

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageDetail(generics.RetrieveAPIView):
    """
    Retrieve a message by its id.
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
