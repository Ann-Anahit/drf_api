from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView  # Import for APIView
from .serializers import GroupSerializer
from .models import Group, Category  # Import Category

class GroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)  # Creator is the authenticated user
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the category by name, falling back if it doesn't exist
        category_name = self.request.data.get("category")
        category = get_object_or_404(Category, name=category_name)
        
        # Save the new group instance with the creator and category
        serializer.save(creator=self.request.user, category=category)
        
        # Automatically add the creator to the group members
        group = serializer.instance
        group.members.add(self.request.user)

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class JoinGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)

        # Check if user is already a member
        if request.user in group.members.all():
            return Response({"detail": "You are already a member of this group."}, status=400)

        # Add user to group members
        group.members.add(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

class LeaveGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)

        # Check if user is not a member
        if request.user not in group.members.all():
            return Response({"detail": "You are not a member of this group."}, status=400)

        # Remove user from group members
        group.members.remove(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
