from rest_framework import viewsets
from .models import PostCategory
from .serializers import PostCategorySerializer

class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all().order_by('name')
    serializer_class = PostCategorySerializer
