from django import forms
from .models import Weapon, Post, Attachment, AttachmentType

class ClassForm(forms.Form):
    post_name = forms.CharField(max_length=30)
    weapon_name = forms.ModelChoiceField(
        queryset=Weapon.objects.all(),  # Fetches all Weapon objects
        empty_label="Select a Weapon"  # Default prompt for the dropdown
    )
    attachment1 = forms.ModelChoiceField(
        queryset=Attachment.objects.all(),
        empty_label="Select Attachment"
    )
    attachment2 = forms.ModelChoiceField(
        queryset=Attachment.objects.all(),
        empty_label="Select Attachment"
    )
    attachment3 = forms.ModelChoiceField(
        queryset=Attachment.objects.all(),
        empty_label="Select Attachment"
    )
    attachment4 = forms.ModelChoiceField(
        queryset=Attachment.objects.all(),
        empty_label="Select Attachment"
    )
    attachment5 = forms.ModelChoiceField(
        queryset=Attachment.objects.all(),
        empty_label="Select Attachment"
    )
