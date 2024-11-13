from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupSerializer
from .models import Group, Category
from drf_api.permissions import IsOwnerOrReadOnly

# List and create groups (GET and POST)
class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Get the category ID from the request data
        category_id = self.request.data.get("category")
        print(f"Received category_id: {category_id}")  # Log the category ID

        if not category_id:
            raise serializers.ValidationError({"detail": "Category ID is required"})

        # Ensure the category exists
        category = get_object_or_404(Category, pk=category_id)
        print(f"Category found: {category}")  # Log the retrieved category

        # Save the group with the creator (authenticated user) and category
        group = serializer.save(creator=self.request.user, category=category)

        # Add the creator as a participant
        group.participants.add(self.request.user)
        print(f"Group created with ID: {group.id}")

# Retrieve, update, or delete a group (GET, PUT, DELETE)
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Join a group (POST)
class JoinGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        if request.user in group.participants.all():
            return Response({"detail": "You are already a member of this group."}, status=status.HTTP_400_BAD_REQUEST)
        group.participants.add(request.user)
        return Response(GroupSerializer(group).data, status=status.HTTP_200_OK)

# Leave a group (POST)
class LeaveGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        if request.user not in group.participants.all():
            return Response({"detail": "You are not a member of this group."}, status=status.HTTP_400_BAD_REQUEST)
        group.participants.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
