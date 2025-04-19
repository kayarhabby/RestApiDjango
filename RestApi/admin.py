from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from RestApi.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    # Display image in admin panel
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/>')
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Team, TeamAdmin)