from django.contrib import admin

from .models import AboutItem, OurTeam


@admin.register(AboutItem)
class AboutItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    pass
