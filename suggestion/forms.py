from django import forms
from django.forms import ModelForm
from .models import Suggestion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        exclude = ['owner', 'treaty']

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Sauvegarder', css_class='btn-primary'))
    helper.form_method = 'POST'