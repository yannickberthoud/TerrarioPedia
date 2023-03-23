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
    BERN_CONVENTION = (
        ('A', 'Annexe I'),
        ('B', 'Annexe II'),
        ('C', 'Annexe III'),
    )
    DIFFICULTIES = (
        ('S', 'Très facile'),
        ('E', 'Facile'),
        ('M', 'Moyen'),
        ('H', 'Difficile'),
        ('V', 'Très difficile')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Famille")
    genus = models.CharField(max_length=64, verbose_name="Genre")
    species = models.CharField(max_length=64, verbose_name="Espèce")
    adult_male_size = models.CharField(max_length=64, verbose_name="Taille adulte mâle")
    adult_female_size = models.CharField(max_length=64, verbose_name="Taille adulte femelle")
    is_cites = models.BooleanField(verbose_name="Enregistré au CITES")
    distribution = models.CharField(max_length=512)
    comments = models.TextField(verbose_name="Commentaire")
    bern_convention = models.CharField(max_length=1, choices=BERN_CONVENTION, verbose_name="Convention de Berne")
    reproduction_type = models.CharField(max_length=1, choices=REPRODUCTION_TYPE, verbose_name="Type de reproduction")
    born_size = models.CharField(max_length=64, verbose_name="Taille des juvéniles")
    main_mores = models.CharField(max_length=1, choices=M_MORES, verbose_name="Moeurs")
    main_activity_period = models.CharField(max_length=1, choices=M_ACTIVITY_Period, verbose_name="Période d'activité")
    preys = models.ManyToManyField(Prey, verbose_name="Proies")
    environments = models.ManyToManyField(Environment, verbose_name="Environnements")
    venom = models.ManyToManyField(Venom, verbose_name="Est venimeux")
    is_poisonous = models.BooleanField(verbose_name="Est vénéneux")
    temperature = models.PositiveIntegerField(verbose_name="Température")
    humidity = models.PositiveIntegerField(verbose_name="Humidité")
    minimal_vivarium_size = models.CharField(max_length=64, help_text="LxlxH", verbose_name="Dimension minimal du terrarium")
    detention_difficulty = models.CharField(max_length=1, choices=DIFFICULTIES, verbose_name="Difficulté de maintien")
    image = models.ImageField(upload_to=card_directory_path)
    slug = models.SlugField(unique=True)

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

