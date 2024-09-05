from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

# List all messages between a user and another user
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get messages exchanged between the authenticated user and another user
        other_user_id = self.kwargs['user_id']
        return Message.objects.filter(
            (models.Q(sender=self.request.user) & models.Q(receiver__id=other_user_id)) |
            (models.Q(sender__id=other_user_id) & models.Q(receiver=self.request.user))
        ).order_by('timestamp')

# Send a new message
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MarkAsReadView(generics.UpdateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        message = Message.objects.get(id=self.kwargs['pk'], receiver=self.request.user)
        return message

    def perform_update(self, serializer):
        serializer.save(is_read=True)
