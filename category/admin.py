from django.contrib import admin
from .models import PostCategory

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumbnail') 

    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}>'
        return 'No Image'
    image_thumbnail.allow_tags = True 
