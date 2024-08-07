from django.contrib import admin

from .models import (AboutItem, Charity, Document, MassMedia, OurTeam,
                     Question, UsefullLink)


@admin.register(AboutItem)
class AboutItemAdmin(admin.ModelAdmin):
    list_display = (
        'indicator', 'info',
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'link',
    )


@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
    )


@admin.register(MassMedia)
class MassMediaAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'link',
    )


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'position',
    )


@admin.register(UsefullLink)
class UsefullLinkAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'link',
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
