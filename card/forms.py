from django import forms
from django.forms import ModelForm
from .models import Card, Amphibian, Lizard
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

class SnakeFilterForm(ModelForm):
    class Meta:
        model = Card
        fields = ('genus', 'species', 'detention_difficulty', 'venom', 'venom_risks')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Filtrer', css_class='btn-primary'))
    help.form_method = 'POST'

class AmphibianFilterForm(ModelForm):
    class Meta:
        model = Amphibian
        fields = ('genus', 'species', 'detention_difficulty', 'call_volume', 'life_community')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Filtrer', css_class='btn-primary'))
    help.form_method = 'POST'

class LizardFilterForm(ModelForm):
    class Meta:
        model = Lizard
        fields = ('genus', 'species', 'detention_difficulty')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Filtrer', css_class='btn-primary'))
    help.form_method = 'POST'

class AmphibianForm(ModelForm):
    class Meta:
        model = Amphibian
        exclude = ['slug', 'approved']

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Sauvegarder', css_class='btn-primary'))
    helper.form_method = 'POST'

class LizardForm(ModelForm):
    class Meta:
        model = Lizard
        exclude = ['slug', 'approved']

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Sauvegarder', css_class='btn-primary'))
    helper.form_method = 'POST'