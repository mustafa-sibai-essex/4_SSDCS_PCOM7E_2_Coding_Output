from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("login_success")
        else:
            return redirect("login_failed")
    else:
        return render(request, "authenticate/gov-login.html", {})

def login_success(request):
    return render(request, "authenticate/login_success.html")

def login_failed(request):
    return render(request, "authenticate/login_failed.html")    