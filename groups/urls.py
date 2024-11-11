from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupListCreate.as_view(), name='group-list-create'),
    path('<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('<int:group_id>/join/', views.JoinGroup.as_view(), name='join-group'),
    path('<int:group_id>/leave/', views.LeaveGroup.as_view(), name='leave-group'),
]
