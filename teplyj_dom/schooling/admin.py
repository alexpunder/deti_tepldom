from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.text import Truncator

from .models import MainGallery, Project, ProjectImage, SendQuestion

admin.site.unregister(Group)
admin.site.unregister(User)


class ProjectImagesInLine(admin.TabularInline):
    model = ProjectImage
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesInLine]
    list_display = (
        'title', 'start_date', 'end_date',
    )
    list_display_links = (
        'title', 'start_date', 'end_date',
    )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SendQuestion)
class SendQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'is_complete', 'name', 'phone', 'email', 'short_subject', 'datetime_to'
    )
    list_display_links = (
        'name', 'phone', 'email',
    )
    list_editable = (
        'is_complete',
    )
    search_fields = (
        'phone', 'email',
    )
    list_filter = (
        'is_complete',
    )
    readonly_fields = (
        'name', 'phone', 'subject', 'email', 'text',
    )

    def short_subject(self, obj):
        return Truncator(obj.subject).words(20)

    def has_add_permission(self, request):
        return False


@admin.register(MainGallery)
class MainGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image',
    )
