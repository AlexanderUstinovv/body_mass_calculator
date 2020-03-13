from django.contrib import admin

from .models import MainPersonData


@admin.register(MainPersonData)
class MainPersonDataAdmin(admin.ModelAdmin):
    fields = (
        'person',
        'name',
        'sex',
        'age',
        'height',
        'weight',
        'smoking'
    )

    list_display = (
        'person',
        'name',
        'sex',
        'age',
        'height',
        'weight',
    )

    readonly_fields = (
        'person',
    )
