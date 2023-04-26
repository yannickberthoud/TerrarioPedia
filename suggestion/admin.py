from django.contrib import admin
from .models import Suggestion

class SuggestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['species', 'suggestion', 'treaty', 'owner',]}),
    ]
    exclude = ('created_at',)

    list_display = ('species', 'suggestion', 'treaty', 'owner', 'created_at')
    list_filter = ('treaty', 'owner', 'species',)

admin.site.register(Suggestion, SuggestionAdmin)