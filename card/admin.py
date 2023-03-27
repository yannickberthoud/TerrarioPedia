from django.contrib import admin
from .models import Category, Venom, Card, CardImage, Prey, Environment

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',]})
    ]
    exclude = ('slug',)
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class VenomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'effects']})
    ]
    list_display = ('name',)

admin.site.register(Venom, VenomAdmin)

class EnvironmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]
    list_display = ('name',)

admin.site.register(Environment, EnvironmentAdmin)

class PreyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', ]})
    ]
    list_display = ('name',)

admin.site.register(Prey, PreyAdmin)

class CardImageAdmin(admin.StackedInline):
    model = CardImage
    extra = 1

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category',]}),
        ('Espèce', {'fields': ['genus', 'species', 'adult_male_size', 'adult_female_size', 'distribution', 'preys', 'comments']}),
        ('Mesure de protection', {'fields': ['is_cites', 'bern_convention']}),
        ('Reproduction', {'fields': ['reproduction_type', 'born_size']}),
        ('Activitées', {'fields': ['environments', 'character', 'main_mores', 'main_activity_period']}),
        ('Morsure et Toxicologie', {'fields': ['dangerosity', 'venom', 'is_poisonous']}),
        ('Terrarium', {'fields': ['detention_difficulty', 'minimal_vivarium_size', 'temperature_high', 'temperature_low', 'humidity']}),
        ('Image', {'fields': ['image']}),
    ]
    exclude = ('slug',)
    list_display = ('genus', 'species')
    list_filter = ('genus',)

admin.site.register(Card, CardAdmin)
