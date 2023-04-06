from django.contrib import admin

from .models import Ads, AdsImage

class AdsImageInline(admin.StackedInline):
    model = AdsImage
    extra = 1

class AdsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner', 'category', 'type_of_ads', 'description']})
    ]
    inlines = [AdsImageInline,]

    list_display = ('owner', 'category', 'type_of_ads', 'created_at')
    search_fields = ['owner', 'description', 'category']
    list_filter = ('category', 'type_of_ads')

admin.site.register(Ads, AdsAdmin)
