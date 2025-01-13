from django.contrib import admin
from .models import PostCategory

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'image')

