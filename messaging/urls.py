from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

# Create the router and register your viewset
router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    # Register the router URLs
    path('', include(router.urls)),  # The router URLs will be available at /api/messages/
]
