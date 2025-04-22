from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import CityForm, RoadForm

# Register your models here.
from RestApi.models import Team, City, Road, RoadSegment, Author, Book

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


class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_display = ('name', 'population', 'location', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    # Display image in admin panel
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"/>')
        return "-"
    image_tag.short_description = 'Image'
    # Display location in admin panel
admin.site.register(City, CityAdmin)

class RoadAdmin(admin.ModelAdmin):
    form = RoadForm
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    # Display geometry in admin panel
    def geometry_tag(self, obj):
        return str(obj.geometry)
    geometry_tag.short_description = 'Geometry'

admin.site.register(Road, RoadAdmin)

class RoadSegmentAdmin(admin.ModelAdmin):
    list_display = ('road', 'start_km', 'end_km', 'status')
    search_fields = ('road__name',)
    list_filter = ('status',)
    ordering = ('road', 'start_km')

    # Display road in admin panel
    def road_tag(self, obj):
        return str(obj.road)
    road_tag.short_description = 'Road'

    # Display status in admin panel
    def status_tag(self, obj):
        return obj.get_status_display()
    status_tag.short_description = 'Status'
    # Display start_km and end_km in admin panel
    def km_tag(self, obj):
        return f"{obj.start_km} km - {obj.end_km} km"
    km_tag.short_description = 'Kilometers'

admin.site.register(RoadSegment, RoadSegmentAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author__name')
    ordering = ('-published_date',)
admin.site.register(Book, BookAdmin)