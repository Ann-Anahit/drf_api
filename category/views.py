from rest_framework import viewsets
from .models import PostCategory
from .serializers import PostCategorySerializer

class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
