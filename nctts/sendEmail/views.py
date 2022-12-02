from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def send_email(request):
    send_mail(
        "Hello there ;)",
        "How you doin ;)",
        None,
        ["contact@m-sibai.com"],
        False
    )
    return render(request, "send/send_email.html")
