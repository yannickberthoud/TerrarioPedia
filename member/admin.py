from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'country', 'profile_picture', 'current_species']}),
    ]

    list_display = ('user', 'country', 'profile_picture', 'current_species')
    list_filter = ('country',)

admin.site.register(Profile, ProfileAdmin)
