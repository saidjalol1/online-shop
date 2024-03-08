from django.contrib import admin

from . import models


@admin.register(models.Positions)
class PositonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Workers)