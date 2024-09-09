from django.urls import path
from .views import MessageListCreate, MessageDetail, MessageUpdateDelete, ConversationList

urlpatterns = [
    path('', MessageListCreate.as_view(), name='message-list-create'),
    path('<int:pk>/', MessageDetail.as_view(), name='message-detail'),
    path('<int:pk>/update-delete/', MessageUpdateDelete.as_view(), name='message-update-delete'),
    path('conversation/<int:receiver_id>/', ConversationList.as_view(), name='conversation-list'),
]
