from django.urls import path 
from . import views

urlpatterns = [
    path("", views.ManageRep, name="ManageReports"),
    path("<int:vuln_id>", views.vulnerability, name="vulnerability")
]