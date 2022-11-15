from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

# Create your views here.

def report(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        vulnerable_website = request.POST['vweb']
        date_time = request.POST['dtg']
        description = request.POST['vdesc']
        replicate = request.POST['vrep']
        exploit_code = request.POST['expcode']
        potential_fix = request.POST['pfix']
        video = request.POST['vlink']
        ins1 = models.PublicUser(first_name=first_name, last_name=last_name, email=email)
        ins2 = models.Vulnerability(vulnerable_website=vulnerable_website, date_time=date_time, description=description, replicate=replicate, exploit_code=exploit_code, potential_fix=potential_fix, video=video, reported_by=email)
        ins1.save()
        ins2.save()
        return redirect("/report/success")

    else:
        return render(request, "report.html")


def success(request):
    return render(request, "success.html")


def delete_info(request):
    return render(request, "delete_info.html")


def delete_success(request):
    return render(request, "delete_success.html")


def view_vulnerabilities(request):
    return render(request, "view_vulnerabilities.html")
