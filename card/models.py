from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.translation import gettext_lazy as _


class Venom(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom")
    effects = models.TextField()

    class Meta:
        verbose_name = 'Toxicologie'
        verbose_name_plural = 'Toxicologies'

    def __str__(self):
        return self.name


def prey_directory_path(instance, filename):
    return 'uploads/images/preys/{0}/{1}'.format(instance.prey.name, filename)


class Prey(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom")

    class Meta:
        verbose_name = 'Proie'
        verbose_name_plural = 'Proies'

    def __str__(self):
        return self.name


class ReproductionPeriod(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Environment(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom")

    class Meta:
        verbose_name = 'Environnement'
        verbose_name_plural = 'Environnements'

    def __str__(self):
        return self.name

def card_directory_path(instance, filename):
    return 'uploads/images/cards/{0}/{1}/{2}'.format(instance.genus, instance.species, filename)

class Card(models.Model):
    DENTITIONS = (
        ('A', 'Aglyphe'),
        ('O', 'Opistoglyphe'),
        ('P', 'Proteroglyphe'),
        ('S', 'Solénoglyphe'),
    )
    M_MORES = (
        ('B', 'Fouisseur'),
        ('T', 'Terrestre'),
        ('S', 'Semi-arboricole'),
        ('A', 'Arboricole')
    )
    M_ACTIVITY_Period = (
        ('N', 'Nocturne'),
        ('T', 'Crépusculaire'),
        ('D', 'Diurne'),
    )
    REPRODUCTION_TYPE = (
        ('O', 'Ovipare'),
        ('V', 'Vivipare'),
        ('I', 'Ovovivipare'),
    )
    DIFFICULTIES = (
        ('S', 'Pour éleveur débutant (premier serpent)'),
        ('E', 'Pour éleveur ayant déjà une base'),
        ('H', 'Pour éleveur expérimenté'),
        ('V', 'Pour éleveur très expérimenté')
    )
    CHARACTERS = (
        ('F', 'Fuyard'),
        ('P', 'Placide'),
        ('C', 'Démonstratif'),
        ('I', 'Irrascible'),
    )
    BITE_DANGEROSITIES = (
        ('I', 'Innofensif'),
        ('C', 'Pouvant entraîner des dommages'),
        ('H', 'Dangereux'),
        ('V', 'Extrêmenent dangereux')
    )
    VENOM_TOXICITIES_RISK = (
        ('F', 'Faible toxicité'),
        ('R', 'Nécessite une surveillance active'),
        ('S', 'Hospitalisation immédiate recommandée'),
        ('D', 'Hospitalisation immédiate (risque de décès)')
    )
    genus = models.CharField(max_length=64, verbose_name="Genre", help_text="Genre")
    species = models.CharField(max_length=64, verbose_name="Espèce", help_text="espèce sous-espèce")
    dentition = models.CharField(max_length=1, verbose_name="Dentition", default='A', choices=DENTITIONS)
    adult_male_size = models.PositiveIntegerField(verbose_name="Taille adulte mâle", help_text="en cm")
    adult_female_size = models.PositiveIntegerField(verbose_name="Taille adulte femelle", help_text="en cm")
    is_cites = models.BooleanField(verbose_name="Enregistré au CITES")
    annex_cites = models.PositiveIntegerField(verbose_name="Annexe CITES", blank=True, default=0, help_text="0 = rien")
    distribution = models.CharField(max_length=512, help_text="Pays où se trouvent l'espèce", verbose_name="Distribution")
    comments = models.TextField(verbose_name="Commentaire", max_length=500, help_text="Maximum 500 caractères")
    reproduction_type = models.CharField(max_length=1, choices=REPRODUCTION_TYPE, verbose_name="Type de reproduction", help_text="Type de reproduction")
    reproduction_period = models.ManyToManyField(ReproductionPeriod, verbose_name="Période de reproduction", help_text="Période de reproduction")
    born_size = models.PositiveIntegerField(verbose_name="Taille des juvéniles", help_text="Taille en cm")
    main_mores = models.CharField(max_length=1, choices=M_MORES, verbose_name="Moeurs", help_text="Moeurs")
    main_activity_period = models.CharField(max_length=1, choices=M_ACTIVITY_Period, verbose_name="Période d'activité", help_text="Période principale d'activité")
    preys = models.ManyToManyField(Prey, verbose_name="Proies", help_text="Proies")
    environments = models.ManyToManyField(Environment, verbose_name="Environnements", help_text="Milieux de vie")
    venom = models.ManyToManyField(Venom, verbose_name="Est venimeux", help_text="Venin(s)")
    venom_risks = models.CharField(max_length=1, verbose_name="niveau de toxicité", help_text="Dangerosité d'une envenimation", choices=VENOM_TOXICITIES_RISK, blank=True)
    behavior = models.CharField(max_length=1, choices=CHARACTERS, verbose_name="Caractère", help_text="Caractère principal en période d'activité")
    dangerosity = models.CharField(max_length=1, choices=BITE_DANGEROSITIES, verbose_name="Dangerosité", help_text="Dangerosité en cas de morsure")
    temperature_high = models.PositiveIntegerField(verbose_name="Température point chaud", help_text="Moyenne haute")
    temperature_low = models.PositiveIntegerField(verbose_name="Température point froid", help_text="Moyenne basse")
    humidity = models.PositiveIntegerField(verbose_name="Humidité", help_text="Humidité moyenne en %")
    minimal_vivarium_size = models.CharField(max_length=11, help_text="LxlxH en cm", verbose_name="Dimension minimale du terrarium")
    detention_difficulty = models.CharField(max_length=1, choices=DIFFICULTIES, verbose_name="Difficulté de maintien", help_text="Pour maintenir l'espèce ou la manipuler")
    image = models.ImageField(upload_to=card_directory_path)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(null=True, verbose_name="Approuvé")

    class Meta:
        verbose_name = 'Serpent'
        verbose_name_plural = 'Serpents'

    def get_scientific_name(self):
        return "{0} {1}".format(self.genus, self.species)

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.genus, self.species)


def amphibian_directory_path(instance, filename):
    return 'uploads/images/amphibians/{0}/{1}/{2}'.format(instance.genus, instance.species, filename)

class Amphibian(models.Model):
    M_MORES = (
        ('B', 'Fouisseur'),
        ('T', 'Terrestre'),
        ('A', 'Arboricole')
    )
    M_ACTIVITY_Period = (
        ('N', 'Nocturne'),
        ('T', 'Crépusculaire'),
        ('D', 'Diurne'),
    )
    DIFFICULTIES = (
        ('S', 'Pour éleveur débutant (premier amphibien)'),
        ('E', 'Pour éleveur ayant déjà une base'),
        ('H', 'Pour éleveur expérimenté'),
        ('V', 'Pour éleveur très expérimenté'),
    )
    CRY_VOL = (
        ('A', 'Aphone'),
        ('D', 'Discret'),
        ('F', 'Bruyant'),
    )
    FAMILIES = (
        ('U', 'Urodèle'),
        ('A', 'Anoure'),
    )
    family = models.CharField(max_length=1, choices=FAMILIES, verbose_name="Famille")
    genus = models.CharField(max_length=64, verbose_name="Genre", help_text="Genre")
    species = models.CharField(max_length=64, verbose_name="Espèce", help_text="espèce sous-espèce")
    adult_male_size = models.PositiveIntegerField(verbose_name="Taille adulte mâle", help_text="en cm")
    adult_female_size = models.PositiveIntegerField( verbose_name="Taille adulte femelle", help_text="en cm")
    is_cites = models.BooleanField(verbose_name="Enregistré au CITES", default=True)
    annex_cites = models.PositiveIntegerField(verbose_name="Annexe CITES", blank=True, default=2, help_text="0 = rien")
    distribution = models.CharField(max_length=512, help_text="Pays où se trouvent l'espèce")
    comments = models.TextField(verbose_name="Commentaire", max_length=500, help_text="Maximum 500 caractères")
    reproduction_period = models.ManyToManyField(ReproductionPeriod, verbose_name="Période de reproduction",
                                                 help_text="Période de reproduction")
    main_mores = models.CharField(max_length=1, choices=M_MORES, verbose_name="Moeurs", help_text="Moeurs")
    main_activity_period = models.CharField(max_length=1, choices=M_ACTIVITY_Period, verbose_name="Période d'activité",
                                            help_text="Période principale")
    call_volume = models.CharField(max_length=1, choices=CRY_VOL, verbose_name="Volume du champs", blank=True)
    preys = models.ManyToManyField(Prey, verbose_name="Proies", help_text="Proies")
    environments = models.ManyToManyField(Environment, verbose_name="Environnements", help_text="Milieux de vie")
    temperature_high = models.PositiveIntegerField(verbose_name="Température point chaud", help_text="Moyenne haute")
    temperature_low = models.PositiveIntegerField(verbose_name="Température point froid", help_text="Moyenne basse")
    humidity = models.PositiveIntegerField(verbose_name="Humidité", help_text="Humidité moyenne en %")
    can_swim = models.BooleanField(verbose_name="Espèce nageuse")
    aquatic_sp = models.BooleanField(verbose_name="Espèce aquatique")
    can_live_in_group = models.BooleanField(verbose_name="Peut vivre en groupe")
    minimal_vivarium_size = models.CharField(max_length=11, help_text="LxlxH en cm",
                                             verbose_name="Dimension minimale du terrarium")
    detention_difficulty = models.CharField(max_length=1, choices=DIFFICULTIES, verbose_name="Difficulté de maintien",
                                            help_text="Pour maintenir l'espèce ou la manipuler")
    image = models.FileField(upload_to=amphibian_directory_path)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(null=True, verbose_name="Approuvé")

    class Meta:
        verbose_name = 'Amphibien'
        verbose_name_plural = 'Amphibiens'

    def get_scientific_name(self):
        return "{0} {1}".format(self.genus, self.species)

    def save(self, *args, **kwargs):
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.genus, self.species)