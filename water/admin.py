from django.contrib import admin
from .models import RunTimes


class RunTimesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['day']}),
        (None,               {'fields': ['v1']}),
        (None,               {'fields': ['v2']}),
        (None,               {'fields': ['v3']}),
        (None,               {'fields': ['v4']}),
        (None,               {'fields': ['v5']}),
        (None,               {'fields': ['v6']}),
        (None,               {'fields': ['v7']}),
        (None,               {'fields': ['pub_date']}),
    ]
    #inlines = [RunTimesInline]
    list_display = ('day', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7')
    list_filter = ['day']
    #extra = 1

admin.site.register(RunTimes, RunTimesAdmin)
