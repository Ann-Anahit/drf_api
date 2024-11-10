from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Group, Category
from .serializers import GroupSerializer


@api_view(['GET'])
def group_list(request):
    """
    List all groups
    """
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def group_detail(request, group_id):
    """
    Get details of a specific group
    """
    group = get_object_or_404(Group, id=group_id)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_group(request):
    """
    Create a new group
    """
    category_name = request.data.get("category")  # The category name is passed in the request
    category = get_object_or_404(Category, name=category_name)  # Fetch the category by name

    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        group = serializer.save(creator=request.user, category=category)  # Assign the category to the group
        group.members.add(request.user)  # Add the creator as the first member
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_group(request, group_id):
    """
    Join an existing group
    """
    group = get_object_or_404(Group, id=group_id)
    
    if request.user in group.members.all():
        return Response({"detail": "You are already a member of this group."}, status=400)

    group.members.add(request.user)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leave_group(request, group_id):
    """
    Leave an existing group
    """
    group = get_object_or_404(Group, id=group_id)

    if request.user not in group.members.all():
        return Response({"detail": "You are not a member of this group."}, status=400)

    group.members.remove(request.user)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer