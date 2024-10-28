from django.urls import path
from .views import MessageListCreate, MessageDetail, MessageUpdateDelete, ConversationList

urlpatterns = [
    path('', MessageListCreate.as_view(), name='message-list-create'),  # Handles GET and POST requests to /messages/
    path('<int:pk>/', MessageDetail.as_view(), name='message-detail'),   # Handles GET, PUT, DELETE for specific messages
    path('<int:pk>/update-delete/', MessageUpdateDelete.as_view(), name='message-update-delete'),  # Update or delete a specific message
    path('conversation/<int:receiver_id>/', ConversationList.as_view(), name='conversation-list'),  # Fetch conversation with a specific receiver
]
