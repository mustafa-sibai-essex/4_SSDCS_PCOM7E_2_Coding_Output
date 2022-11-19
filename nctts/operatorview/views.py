from django.http import HttpResponse
from django.shortcuts import render
from .models import VulnerabilitiesOP

# Create your views here.

def ManageRep(request):
    return render(request, "operatorview/managereport.html", {"vulnerabilities": VulnerabilitiesOP.objects.all()})

def vulnerability(request, vuln_id):
    vulnerability = VulnerabilitiesOP.objects.get(pk=vuln_id)
    return render(request, "operatorview/vulnerability.html", {"vulnerability": vulnerability})

