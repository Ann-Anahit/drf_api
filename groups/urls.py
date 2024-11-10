from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/groups/category/<str:category_name>/', group_list_by_category),
    path('api/', include(router.urls)),
]
