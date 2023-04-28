from django.forms import ModelForm
from django import forms
from .models import Ads
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_countries.fields import CountryField

class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = ('category', 'type_of_ads', 'description', 'image')
        exclude = ('created_at',)
        widgets = {
            'image': forms.ClearableFileInput(attrs={"multiple": True}),
            #'owner': forms.HiddenInput(),
        }
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Publier mon annonce', css_class='btn-primary'))
    help.form_method = 'POST'