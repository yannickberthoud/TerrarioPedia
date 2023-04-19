from django.contrib import admin
from .models import Venom, Card, Prey, Environment, ReproductionPeriod, Amphibian, AmphibianLifeCommunity

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

class ReproductionPeriodAdmion(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',]})
    ]
    list_display = ('name', )

admin.site.register(ReproductionPeriod, ReproductionPeriodAdmion)

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Espèce', {'fields': ['genus', 'species', 'is_cites', 'annex_cites']}),
        ('Caractéristiques', {'fields': ['dentition', 'adult_male_size', 'adult_female_size', 'distribution', 'preys', 'comments']}),
        ('Reproduction', {'fields': ['reproduction_type', 'reproduction_period', 'born_size']}),
        ('Activitées', {'fields': ['environments', 'behavior', 'main_mores', 'main_activity_period']}),
        ('Morsure et Toxicologie', {'fields': ['dangerosity', 'venom', 'venom_risks']}),
        ('Terrarium', {'fields': ['detention_difficulty', 'minimal_vivarium_size', 'temperature_high', 'temperature_low', 'humidity']}),
        ('Image', {'fields': ['image']}),
        ('Approbation', {'fields': ['approved']}),
    ]
    exclude = ('slug',)
    list_display = ('genus', 'species', 'approved')
    search_fields = ['genus', 'species', 'environments__name', 'venom__name', 'temperature_high', 'temperature_low', 'humidity', \
                     'minimal_vivarium_size']
    list_filter = ('genus',)

admin.site.register(Card, CardAdmin)

class AmphibianLifeCommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', ]})
    ]
    list_display = ('name',)


admin.site.register(AmphibianLifeCommunity, AmphibianLifeCommunityAdmin)

class AmphibienAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['family',]}),
        ('Espèce', {'fields': ['genus', 'species', 'adult_male_size', 'adult_female_size', 'distribution', 'preys', 'comments']}),
        ('Mesure de protection', {'fields': ['is_cites', 'annex_cites']}),
        ('Reproduction', {'fields': ['reproduction_period']}),
        ('Activitées', {'fields': ['environments', 'main_mores', 'main_activity_period', 'call_volume']}),
        ('Terrarium', {'fields': ['detention_difficulty', 'minimal_vivarium_size', 'temperature_high', 'temperature_low', 'humidity', 'life_community']}),
        ('Aquatique', {'fields': ['can_swim', 'aquatic_sp']}),
        ('Image', {'fields': ['image']}),
        ('Approbation', {'fields': ['approved']}),
    ]
    exclude = ('slug',)
    list_display = ('genus', 'species', 'approved')
    search_fields = ['genus', 'species', 'environments__name', 'temperature_high', 'temperature_low', 'humidity', 'minimal_vivarium_size']
    list_filter = ('genus',)

admin.site.register(Amphibian, AmphibienAdmin)
