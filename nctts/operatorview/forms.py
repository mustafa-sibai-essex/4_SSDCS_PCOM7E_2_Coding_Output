from django.forms import ModelForm
from report.models import Vulnerabilities

class CreateNewVuln(ModelForm):
    class Meta:
        model = Vulnerabilities
        fields = '__all__'
