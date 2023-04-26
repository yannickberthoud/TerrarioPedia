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
    profile_picture = forms.ImageField(label="Photo de profil", widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)

    current_species = forms.CharField(label="Vos espèces actuelles", help_text="Une espèce par ligne",
                                    widget=forms.Textarea(attrs={"rows": "5"}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['current_species'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ("country", "profile_picture", "current_species")
        widgets = {
            "country": CountrySelectWidget(attrs={"class": "form-select"}),
            'profile_picture': forms.ClearableFileInput(attrs={'multiple': False})
        }