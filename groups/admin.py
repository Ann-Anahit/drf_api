from django.contrib import admin
from .models import Group, Category

admin.site.register(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)