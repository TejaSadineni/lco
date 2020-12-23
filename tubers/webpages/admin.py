from django.contrib import admin
from .models import Slider , Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','role','created_date')
    list_display_links = ('id','first_name')
    list_filter = ('role',)
    search_fields = ('first_name',)

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
