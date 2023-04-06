from django import forms
from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget

from .models import Ads, AdsImage
class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'
        exclude = ('created_at', 'owner')

class AdsImageForm(ModelForm):
    class Meta:
        model = AdsImage
        fields = '__all__'