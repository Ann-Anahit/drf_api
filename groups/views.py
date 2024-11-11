from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupSerializer
from .models import Group, Category

# Create a new group (POST method) for authenticated users
class GroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Group, Category
from .serializers import GroupSerializer

class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Retrieve the category ID from the request data
        category_id = self.request.data.get("category")
        if not category_id:
            return Response({"detail": "Category ID is required"}, status=400)

        try:
            # Retrieve the Category object using the provided category_id
            category = get_object_or_404(Category, pk=category_id)
        except Exception as e:
            return Response({"detail": f"Error retrieving category: {str(e)}"}, status=500)

        # Save the new group instance with the creator and category
        try:
            serializer.save(creator=self.request.user, category=category)
        except Exception as e:
            return Response({"detail": f"Error saving group: {str(e)}"}, status=500)

        # Add the creator as the first participant
        group = serializer.instance
        try:
            group.participants.add(self.request.user)
        except Exception as e:
            return Response({"detail": f"Error adding creator to group: {str(e)}"}, status=500)

        # Return the created group data
        return Response(serializer.data, status=201)
        # Save the new group with the creator and category
        serializer.save(creator=self.request.user, category=category)
        
        # Add the creator as the first participant
        group = serializer.instance
        group.participants.add(self.request.user)
        print(f"Group created with ID {group.id} and category {category.name}")

# Retrieve, update, or delete a group (GET, PUT, DELETE methods)
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

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
