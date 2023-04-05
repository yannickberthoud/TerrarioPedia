from django.db import models

class Ads(models.Model):
    CATEGORIES = (
        ('R', 'Recherches'),
        ('V', 'Vends')
    )
    category = models.CharField(max_length=1, choices=CATEGORIES)
    description = models.TextField()

    def __str__(self):
        return self.description

class AdsImage(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/{users}/ads/')

    def __str__(self):
        return self.image