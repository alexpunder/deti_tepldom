from django.contrib import admin

from .models import Blog, Category, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'pub_date', 'title', 'category',
    )
    list_select_related = (
        'category',
    )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
