from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'country']}),
    ]

    list_display = ('user', 'country')
    list_filter = ('country',)

admin.site.register(Profile, ProfileAdmin)
