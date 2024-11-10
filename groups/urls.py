# groups/urls.py

from django.urls import path
from .views import GroupListCreate, GroupDetail  # Ensure you import the correct views

urlpatterns = [
    path('', GroupListCreate.as_view(), name='group-list-create'),  # URL for the list and create view
    path('<int:pk>/', GroupDetail.as_view(), name='group-detail'),  # URL for the detail view
]