from django import forms
from django.forms import ModelForm
from .models import Card, Amphibien
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

def card_directory_path(instance, filename):
    return 'uploads/images/cards/{0}/{1}/{2}'.format(instance.genus, instance.species, filename)
class SnakeForm(ModelForm):
    class Meta:
        model = Card
        exclude = ['slug', 'approved']

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Sauvegarder', css_class='btn-primary'))
    helper.form_method = 'POST'

class AmphibianForm(ModelForm):
    class Meta:
        model = Amphibien
        exclude = ['slug', 'approved']

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Sauvegarder', css_class='btn-primary'))
    helper.form_method = 'POST'
