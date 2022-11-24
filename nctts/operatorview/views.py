from django.http import HttpResponse
from django.shortcuts import render, redirect
from report.models import Vulnerabilities
from.forms import CreateNewVuln
from django.db.models import Q


# Create your views here.

def ManageRep(request):
    countAA= Vulnerabilities.objects.filter(status="Awaiting Approval").count
    countEs= Vulnerabilities.objects.filter(status="Escalated").count
    context = {'countAA':countAA, 'countEs':countEs, "vulnerabilities": Vulnerabilities.objects.all()}
    return render(request, "operatorview/managereport.html", context)

def vulnerability(request, vuln_id):
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    return render(request, "operatorview/vulnerability.html", {"vulnerability": vulnerability})

def Add_new(request):
    form=CreateNewVuln()
    if request.method == 'POST':
        form = CreateNewVuln(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ManageReports")
    return render(request, "operatorview/Add_new.html", {"form":form})

def updatevuln(request, vuln_id):
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    form=CreateNewVuln(instance = vulnerability)
    if request.method == 'POST':
        form = CreateNewVuln(request.POST, instance = vulnerability)
        if form.is_valid():
            form.save()
            return redirect("ManageReports")
    return render(request, "operatorview/Add_new.html", {"form":form})

def Delete(request, vuln_id):
    vulnerability = Vulnerabilities.objects.get(pk=vuln_id)
    if request.method == "POST":
        vulnerability.delete()
        return redirect("ManageReports")
    return render(request, "operatorview/delete.html", {"vulnerability": vulnerability})


def Awaiting(request):
    return render(request, "operatorview/awaiting.html", {"vulnerabilities": Vulnerabilities.objects.filter(status="Awaiting Approval")})

def Escalated(request):
    return render(request, "operatorview/escalate.html", {"vulnerabilities": Vulnerabilities.objects.filter(status="Escalated")})

def searchresults(request):
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get(str('search'))
        vulnerabilities = Vulnerabilities.objects.filter(Q(status=query) | Q(assigned_to=query))
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})

def searchreference(request):
    vulnerabilities = []
    if request.method == 'GET':
        query = request.GET.get('search')
        vulnerabilities = Vulnerabilities.objects.filter(vul_no=query)
    return render(request, "operatorview/searchresults.html", {'query':query, 'vulnerabilities':vulnerabilities})