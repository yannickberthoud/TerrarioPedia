from django.contrib import admin
from .models import Ads

class AdsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner',]}),
        ('Annonce', {'fields': ['description', 'image']}),
    ]
    exclude =('created_at',)
    list_display = ('owner', 'description', 'created_at')
    search_fields = ['owner', 'description', 'created_at']
    list_filter = ('owner',)

admin.site.register(Ads, AdsAdmin)