from django.contrib import admin
from .models import Faq

class FaqAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category', 'question', 'answer']})
    ]

    list_display = ('category', 'question')

admin.site.register(Faq, FaqAdmin)