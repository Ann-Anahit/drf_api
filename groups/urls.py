# urls.py in your Django app
from django.urls import path
from .views import GroupListCreate, GroupDetail

urlpatterns = [
    # Ensure the path is correct and matches your API structure
    path('api/groups/', GroupListCreate.as_view(), name='group-list-create'),  # Handles GET and POST
    path('api/groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),  # Handles GET for a single group
]
