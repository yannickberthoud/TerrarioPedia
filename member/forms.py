from django import forms
from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget

from django.contrib.auth.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].widget.attrs['class'] = 'form-control invisible'
    class Meta:
        model = Profile
        fields = ("country", "user")
        widgets = {
            "country": CountrySelectWidget(attrs={"class": "form-select"})
        }