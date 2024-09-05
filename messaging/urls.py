from django.urls import path
from .views import MessageListView, MessageCreateView, MarkAsReadView 

urlpatterns = [
    # List messages exchanged with a specific user
    path('messages/<int:user_id>/', MessageListView.as_view(), name='message-list'),

    # Send a new message
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),

    path('messages/read/<int:pk>/', MarkAsReadView.as_view(), name='message-read'),
]
