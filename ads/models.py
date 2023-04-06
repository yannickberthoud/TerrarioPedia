import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from card.models import Category

def ads_directory_path(instance, filename):
    return 'uploads/{0}/images/ads/{1}'.format(instance.ads.owner, filename)
class Ads(models.Model):
    TYPE_OF_ADS = (
        ('R', 'Recherche'),
        ('V', 'Vends')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    type_of_ads = models.CharField(max_length=1, choices=TYPE_OF_ADS)
    description = models.TextField()

    def __str__(self):
        return self.description



class AdsImage(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=ads_directory_path, blank=True, null=True)

    def __str__(self):
        return f"{self.image}"