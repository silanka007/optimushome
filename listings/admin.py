from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'address', 'city', 'price', 'list_date')
    list_filter = ('realtor', 'state')
    list_editable = ('is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'city', 'state', 'address', 'price')
    list_per_page = 10


# Register your models here.
admin.site.register(Listing, ListingAdmin)
