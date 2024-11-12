from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupSerializer
from .models import Group, Category
from drf_api.permissions import IsOwnerOrReadOnly  

class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Check for category in the request data
        category_id = self.request.data.get("category")
        if not category_id:
            return Response({"detail": "Category ID is required"}, status=400)

        category = get_object_or_404(Category, pk=category_id)

        # Save the new group instance with the creator and category
        group = serializer.save(creator=self.request.user, category=category)

        # Add the creator as the first participant
        group.participants.add(self.request.user)

        return Response(serializer.data, status=201)

# Retrieve, update, or delete a group (GET, PUT, DELETE methods)
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Join a group (POST method)
class JoinGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        # Retrieve the group by id
        group = get_object_or_404(Group, id=group_id)

        # Check if the user is already a member of the group
        if request.user in group.participants.all():
            return Response({"detail": "You are already a member of this group."}, status=400)

        # Add the user to the group participants
        group.participants.add(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

# Leave a group (POST method)
class LeaveGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        # Retrieve the group by id
        group = get_object_or_404(Group, id=group_id)

        # Check if the user is not a member of the group
        if request.user not in group.participants.all():
            return Response({"detail": "You are not a member of this group."}, status=400)

        # Remove the user from the group participants
        group.participants.remove(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
