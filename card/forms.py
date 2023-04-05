from django import forms
from django.forms import ModelForm
from .models import Card

def card_directory_path(instance, filename):
    return 'uploads/images/cards/{0}/{1}/{2}'.format(instance.genus, instance.species, filename)
class CardForm(ModelForm):
    class Meta:
        model = Card
        exclude = ['slug', 'approved']
