from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

urlpatterns = [
    path('', root_route),  # Root route
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # DRF authentication URLs
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # DJ REST Auth URLs
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # DJ REST Auth Registration URLs
    path('dj-rest-auth/logout/', logout_route),  # Custom logout route

    # Include app-specific URLs
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    path('messages/', include('messaging.urls')),
]
