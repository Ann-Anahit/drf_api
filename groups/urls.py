from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupListCreate.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('groups/<int:group_id>/join/', views.JoinGroup.as_view(), name='join-group'),
    path('groups/<int:group_id>/leave/', views.LeaveGroup.as_view(), name='leave-group'),
]