from django.forms import ModelForm
from django import forms
from report.models import Vulnerabilities

class CreateNewVuln(ModelForm):
    class Meta:
        model = Vulnerabilities
        fields = '__all__'

