from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


def photo_directory_path(instance, filename):
    return 'uploads/images/member/{0}/photos/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField(verbose_name="Pays", blank=True)
    profile_picture = models.ImageField(upload_to=photo_directory_path, verbose_name="Photo de profil", blank=True, null=True)
    current_species = models.TextField(verbose_name="Vos espèces actuelles", help_text="Une espèce par ligne", blank=True, null=True)

    def __str__(self):
        return self.country.name\

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)\

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()