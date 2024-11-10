from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Group, Category
from .serializers import GroupSerializer

class GroupCreate(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # You can also automatically assign the creator as a member of the group
        category = Category.objects.get(name=self.request.data["category"])
        serializer.save(creator=self.request.user, category=category)
