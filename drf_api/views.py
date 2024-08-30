from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE,
)

@api_view(['GET'])
@permission_classes([AllowAny])
def root_route(request):
    return Response({"message": "Welcome to the API!"})
