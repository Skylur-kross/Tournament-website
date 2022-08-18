from django import forms
# from pages.models import *

from src.pages.models import players


class UserForm(forms.ModelForm):
    class Meta:
        model= players
        fields='__all__'