from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Event

class EventAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    fields = ['title', 'start_date', 'end_date', 'image', 'published', 'listed', 'summary', 'slug']
    list_filter = ['start_date']
    list_display = ['title', 'start_date', 'end_date', 'published', 'listed']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}
    save_as = True


admin.site.register(Event, EventAdmin)
