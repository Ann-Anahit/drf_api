from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupListCreate, GroupDetail, JoinGroup, LeaveGroup, GroupViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path('join/<int:group_id>/', JoinGroup.as_view(), name='join-group'),
    path('leave/<int:group_id>/', LeaveGroup.as_view(), name='leave-group'),
    path('<int:group_id>/', GroupDetail.as_view(), name='group-detail'),
]
