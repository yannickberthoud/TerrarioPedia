from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom")
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Famille'
        verbose_name_plural = 'Familles'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

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
        ('S', 'Très facile'),
        ('E', 'Facile'),
        ('M', 'Moyen'),
        ('H', 'Difficile'),
        ('V', 'Très difficile')
    )
    CHARACTERS = (
        ('F', 'Fuyard'),
        ('P', 'Placide'),
        ('M', 'Mordeur'),
        ('D', 'Démonstratif'),
        ('C', 'Caractérielle'),
        ('I', 'Irritable'),
        ('A', 'Agressif')
    )
    DANGEROSITIES = (
        ('I', 'Inoffensif'),
        ('L', 'Sans danger'),
        ('C', 'Pouvant entraîner des dommages'),
        ('H', 'Dangereux'),
        ('V', 'Extrêmenent dangereux')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Famille")
    genus = models.CharField(max_length=64, verbose_name="Genre", help_text="Genre")
    species = models.CharField(max_length=64, verbose_name="Espèce", help_text="espèce sous-espèce")
    adult_male_size = models.CharField(max_length=64, verbose_name="Taille adulte mâle", help_text="en cm")
    adult_female_size = models.CharField(max_length=64, verbose_name="Taille adulte femelle", help_text="en cm")
    is_cites = models.BooleanField(verbose_name="Enregistré au CITES")
    annex_cites = models.PositiveIntegerField(verbose_name="Annexe CITES", blank=True, default=0, help_text="0 = rien")
    distribution = models.CharField(max_length=512, help_text="Pays où se trouvent l'espèce")
    comments = models.TextField(verbose_name="Commentaire", max_length=250, help_text="Maximum 250 caractères")
    reproduction_type = models.CharField(max_length=1, choices=REPRODUCTION_TYPE, verbose_name="Type de reproduction", help_text="Type de reproduction")
    reproduction_period = models.ManyToManyField(ReproductionPeriod, verbose_name="Période de reproduction", help_text="Période de reproduction")
    born_size = models.CharField(max_length=64, verbose_name="Taille des juvéniles", help_text="Taille en cm")
    main_mores = models.CharField(max_length=1, choices=M_MORES, verbose_name="Moeurs", help_text="Moeurs")
    main_activity_period = models.CharField(max_length=1, choices=M_ACTIVITY_Period, verbose_name="Période d'activité", help_text="Période principale")
    preys = models.ManyToManyField(Prey, verbose_name="Proies", help_text="Proies")
    environments = models.ManyToManyField(Environment, verbose_name="Environnements", help_text="Milieux de vie")
    venom = models.ManyToManyField(Venom, verbose_name="Est venimeux", help_text="Venin(s)")
    is_poisonous = models.BooleanField(verbose_name="Est vénéneux", help_text="L'espèce est vénéneuse dans la nature")
    character = models.CharField(max_length=1, choices=CHARACTERS, help_text="Caractère principale en période d'activité")
    dangerosity = models.CharField(max_length=1, choices=DANGEROSITIES, help_text="Dangerosité en cas d'attaque")
    temperature_high = models.PositiveIntegerField(verbose_name="Température point chaud", help_text="Moyenne haute")
    temperature_low = models.PositiveIntegerField(verbose_name="Température point froid", help_text="Moyenne basse")
    humidity = models.PositiveIntegerField(verbose_name="Humidité", help_text="Humidité moyenne en %")
    minimal_vivarium_size = models.CharField(max_length=64, help_text="LxlxH en cm", verbose_name="Dimension minimal du terrarium")
    detention_difficulty = models.CharField(max_length=1, choices=DIFFICULTIES, verbose_name="Difficulté de maintien", help_text="Pour maintenir l'espèce ou la manipuler")
    image = models.ImageField(upload_to=card_directory_path)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Espèce'
        verbose_name_plural = 'Espèces'

    def get_scientific_name(self):
        return "{0} {1}".format(self.genus, self.species)

    def save(self, *args, **kwargs):
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.genus, self.species)

class CardImage(models.Model):
    PHASES = (
        ('J', 'Juvénile'),
        ('S', 'Sub-adulte'),
        ('A', 'Adulte')
    )
    SEX = (
        ('U', 'Indéfini'),
        ('M', 'Male'),
        ('F', 'Femelle')
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="Espèce")
    image = models.ImageField(upload_to=card_directory_path)
    phase = models.CharField(max_length=1, choices=PHASES, blank=True)
    sex = models.CharField(max_length=1, choices=SEX, blank=True, verbose_name="Sexe")
    locality = models.CharField(max_length=512, blank=True, verbose_name="Localité")
    comments = models.TextField(help_text="mutation, morphotype, hybridation", blank=True, verbose_name="Commentaire")

    def __str__(self):
        return "{0}".format(self.image)

