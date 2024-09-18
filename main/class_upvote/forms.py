from django import forms
from .models import Weapon

class ClassForm(forms.Form):
    weapon_name = forms.ModelChoiceField(
        queryset=Weapon.objects.all(),  # Fetches all Weapon objects
        empty_label="Select a Weapon",  # Default prompt for the dropdown
    )