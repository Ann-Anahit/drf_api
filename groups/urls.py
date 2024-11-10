from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, group_list, group_detail, create_group, join_group, leave_group

router = DefaultRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/groups/', group_list),  # Endpoint for listing all groups
    path('api/groups/<int:group_id>/', group_detail),  # Endpoint for group details
    path('api/groups/create/', create_group),  # Endpoint for creating groups
    path('api/groups/<int:group_id>/join/', join_group),  # Endpoint for joining a group
    path('api/groups/<int:group_id>/leave/', leave_group),  # Endpoint for leaving a group
    path('api/', include(router.urls)),  # Include the router-generated URLs for GroupViewSet
]
