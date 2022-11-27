from django.http import HttpResponse
from django.shortcuts import render, redirect
from report.models import Vulnerabilities
from django.contrib.auth.decorators import login_required
from.forms import CreateNewVuln
from django.db.models import Q


# Create your views here.
#function to open the manage report view. Supplies the template with contents of vulnerability model and other required data
@login_required
def ManageRep(request):
    countAA= Vulnerabilities.objects.filter(status="Awaiting Approval").count
    context = {'countAA':countAA, "vulnerabilities": Vulnerabilities.objects.all()}
    return render(request, "operatorview/managereport.html", context)

@login_required
def vulnerability(request, vuln_id):
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    return render(request, "operatorview/vulnerability.html", {"vulnerability": vulnerability})

@login_required
def Add_new(request):
    form=CreateNewVuln()
    if request.method == 'POST':
        form = CreateNewVuln(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ManageReports")
    return render(request, "operatorview/Add_new.html", {"form":form})

@login_required
def updatevuln(request, vuln_id):
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
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    if request.method == "POST":
        vulnerability.delete()
        return redirect("ManageReports")
    return render(request, "operatorview/delete.html", {"vulnerability": vulnerability})

@login_required
def Awaiting(request):
    return render(request, "operatorview/awaiting.html", {"vulnerabilities": Vulnerabilities.objects.filter(status="Awaiting Approval")})

@login_required
def searchresults(request):
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get(str('search'))
        vulnerabilities = Vulnerabilities.objects.filter(Q(status=query) | Q(assigned_to=query))
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})

@login_required
def searchreference(request):
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get('search')
        if query != "":
            vulnerabilities = Vulnerabilities.objects.filter(vul_no=query)
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})