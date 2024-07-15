from django.contrib import admin

from .models import SendQuestion, Project


@admin.register(SendQuestion)
class SendQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
