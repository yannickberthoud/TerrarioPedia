from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    species = models.CharField(max_length=200, verbose_name="Espèce")
    suggestion = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    treaty = models.BooleanField(default=False, verbose_name="Traité")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.species} a une suggestion"
