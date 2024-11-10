from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Group, Category
from .serializers import GroupSerializer
from rest_framework.decorators import permission_classes

class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Handle category selection and group creation
        category_name = self.request.data.get("category")
        category = get_object_or_404(Category, name=category_name)
        serializer.save(creator=self.request.user, category=category)
        group = serializer.instance
        group.members.add(self.request.user)  # Add creator as the first member

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Class-Based View to Join an Existing Group
class JoinGroup(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)

        if request.user in group.members.all():
            return Response({"detail": "You are already a member of this group."}, status=400)

        group.members.add(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


# Class-Based View to Leave an Existing Group
class LeaveGroup(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)

        if request.user not in group.members.all():
            return Response({"detail": "You are not a member of this group."}, status=400)

        group.members.remove(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


# Group ViewSet to Handle CRUD Operations
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
