from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def report(request):
    return render(request, "report.html")


def success(request):
    return render(request, "success.html")


def delete_info(request):
    return render(request, "delete_info.html")


def delete_success(request):
    return render(request, "delete_success.html")


def view_vulnerabilities(request):
    return render(request, "view_vulnerabilities.html")
