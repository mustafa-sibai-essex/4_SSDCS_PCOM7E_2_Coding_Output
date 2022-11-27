from django.forms import ModelForm
from django import forms
from report.models import Vulnerabilities

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class CreateNewVuln(ModelForm):
    class Meta:
        model = Vulnerabilities
        fields = ['status', 'assigned_to', 'reported_by', 'vulnerable_website', 'date_time', 'description', 'replicate', 'exploit_code', 'potential_fix', 'video']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class':'form-control'})

        self.fields['assigned_to'].widget.attrs.update({'class':'form-control'})

        self.fields['reported_by'].widget.attrs.update({'class':'form-control'})

        self.fields['vulnerable_website'].label = 'Vulnerable website link:'
        self.fields['vulnerable_website'].widget.attrs.update({'class':'form-control'})
        
        self.fields['date_time'].label = 'The date and time the incident occured: '
        self.fields['date_time'].widget = DateTimeInput()
        self.fields['description'].widget.attrs.update({'class':'form-control'})

        self.fields['description'].label = 'Description of vulnerability:'
        self.fields['description'].widget.attrs.update({'class':'form-control', 'rows':'3'})
        
        self.fields['replicate'].label = 'How to replicate the vulnerability:'
        self.fields['replicate'].widget.attrs.update({'class':'form-control', 'rows':'3'})

        self.fields['exploit_code'].label = 'Exploit code (if available):'
        self.fields['exploit_code'].widget.attrs.update({'class':'form-control', 'rows':'3'})

        self.fields['potential_fix'].label = 'Potential fix for the issue (Optional):'
        self.fields['potential_fix'].widget.attrs.update({'class':'form-control', 'rows':'3'})

        self.fields['video'].label = 'Link to video replicating the problem (Optional):'
        self.fields['video'].widget.attrs.update({'class':'form-control'})