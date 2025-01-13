from django.urls import path
from .views import PostCategoryListView

urlpatterns = [
    path('postcategories/', PostCategoryListView.as_view(), name='postcategories'),
]
