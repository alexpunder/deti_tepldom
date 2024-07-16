from django.contrib import admin

from .models import Blog, Tag, Category


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
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
