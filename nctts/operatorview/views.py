from django.http import HttpResponse
from django.shortcuts import render, redirect
from report.models import *
from django.contrib.auth.decorators import login_required
from.forms import CreateNewVuln
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import models


# Create your views here.

@login_required
def ManageRep(request):
    """Renders the Main operator template (managereport)"""
    # also supplies the manage report template with the countAA variable and details of all vulnerabilities from the model
    countAA= Vulnerabilities.objects.filter(status="Awaiting Approval").count
    context = {'countAA':countAA, "vulnerabilities": Vulnerabilities.objects.all()}
    return render(request, "operatorview/managereport.html", context)


@login_required
def vulnerability(request, vuln_id):
    """Render the vulnerabilty template - contains all data on an individual vulnerability"""
    # provides the template with details of a specific vulnerability using the vulnerability ID
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    return render(request, "operatorview/vulnerability.html", {"vulnerability": vulnerability})


@login_required
def Add_new(request):
    """Render the Add new vulnerability page - in Operator view"""
    op = request.user

    #uses the currently logged in Operator to auto fill the Reported_by details
    #requires operator details to exist in the PublicUser model
    #first it checks if this operator has a profile in the PublicUser table and adds a new profile if required
    try:
        duplicate_check = PublicUser.objects.get(first_name = op)
    except ObjectDoesNotExist:
        ins_user = PublicUser(first_name= op)
        ins_user.save()
    except MultipleObjectsReturned:
        pass  
        
    operator = PublicUser.objects.get(first_name = op)

    form=CreateNewVuln()
    if request.method == 'POST':
        """ this function will save the completed form as a new vulnerability record in the model."""
        form = CreateNewVuln(request.POST)
        if form.is_valid():
            vul = form.save()
            vul.reported_by= operator         
            vul.save()
            return redirect("ManageReports")
    return render(request, "operatorview/Add_new.html", {"form":form})


@login_required
def updatevuln(request, vuln_id):
    """Uses the vuln-id of an existing record to auto-fill the Add new template and allows us to update record"""
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    form=CreateNewVuln(instance = vulnerability)
    if request.method == 'POST':
        form = CreateNewVuln(request.POST, instance = vulnerability)
        if form.is_valid():
            form.save()
            return redirect("ManageReports")
    return render(request, "operatorview/Add_new.html", {"form":form})

@login_required
def Delete(request, vuln_id):
    """Allows us to delete a vulnerability"""
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    if request.method == "POST":
        vulnerability.delete()
        return redirect("ManageReports")
    return render(request, "operatorview/delete.html", {"vulnerability": vulnerability})

@login_required
def Awaiting(request):
    """Performs a search of the vulnerabilities awaiting approval and displays them in a template"""
    return render(request, "operatorview/awaiting.html", {"vulnerabilities": Vulnerabilities.objects.filter(status="Awaiting Approval")})

@login_required
def searchresults(request):
    """Performs a search of the vulnerabilities by status or assigned department and displays them in a template"""
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get(str('search'))
        vulnerabilities = Vulnerabilities.objects.filter(Q(status=query) | Q(assigned_to=query))
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})

@login_required
def searchreference(request):
    """Performs a search of the vulnerabilities by ID and displays them in a template"""
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get('search')
        if query != "":
            vulnerabilities = Vulnerabilities.objects.filter(vul_no=query)
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})