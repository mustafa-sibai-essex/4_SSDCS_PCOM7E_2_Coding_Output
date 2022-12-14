from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account


class HomeView(TemplateView):
    template_name = "homepage/home.html"

def get_ip_address(request):
    """Returns the client IP address when they make a request"""

    x_forwarded_for = request.META.get("HTTP_X_REAL_IP")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    elif request.META.get("HTTP_X_REAL_IP"):
        ip = request.META.get("HTTP_X_REAL_IP")
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def login_user(request):
    """Allow the user to login with their username and password. If the user is an admin they will be directed to the admin page. If the user is an operator they will be directed to the operator page."""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:

            allow_login = False

            try:
                userAccountIp = Account.objects.get(user_id=user.id)
                ip_addresses = userAccountIp.ip_addresses.replace(" ", "").split(",")
                current_ip_address = get_ip_address(request)

                for ip in ip_addresses:
                    if current_ip_address == ip:
                        allow_login = True
                        break
            except Account.DoesNotExist:
                pass

            login(request, user)
            if user.is_superuser:
                return redirect("admin:index")
            else:
                if allow_login:
                    return redirect("ManageReports")
                else:
                    return render(request, "authenticate/unknow-ip-login.html")
        else:
            return redirect("homepage:login_failed")
    else:
        return render(request, "authenticate/gov-login.html", {})


def login_success(request):
    """Returns a success login page"""
    return render(request, "authenticate/login_success.html")


def login_failed(request):
    """Returns a failed login page"""
    return render(request, "authenticate/login_failed.html")
