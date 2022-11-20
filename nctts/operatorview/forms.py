from django.forms import ModelForm
from django import forms
from .models import VulnerabilitiesOP

class CreateNewVuln(ModelForm):
    class Meta:
        model = VulnerabilitiesOP
        fields = '__all__'

