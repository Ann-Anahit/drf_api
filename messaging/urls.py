from django.urls import path
from .views import MessageListView, MessageCreateView, MarkAsReadView

urlpatterns = [
    path('<int:user_id>/', MessageListView.as_view(), name='message-list'),
    path('create/', MessageCreateView.as_view(), name='message-create'),
    path('read/<int:pk>/', MarkAsReadView.as_view(), name='message-read'),
]
