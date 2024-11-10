from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from rest_framework.authtoken.views import obtain_auth_token

from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', root_route),  # Root route
    path('admin/', admin.site.urls),  # Django admin interface

    # Authentication URLs
    path('api-auth/', include('rest_framework.urls')),  # DRF auth
    path('dj-rest-auth/logout/', logout_route),  # Custom logout route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # dj-rest-auth for login, password reset, etc.
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # dj-rest-auth registration

    # App-specific URLs
    path('profiles/', include('profiles.urls')),  # Profiles app
    path('posts/', include('posts.urls')),  # Posts app
    path('comments/', include('comments.urls')),  # Comments app
    path('likes/', include('likes.urls')),  # Likes app
    path('followers/', include('followers.urls')),  # Followers app
    path('groups/', include('groups.urls')),  # Groups app
]







    
