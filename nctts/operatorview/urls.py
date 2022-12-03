from django.urls import path
from . import views

urlpatterns = [
    path("", views.ManageRep, name="ManageReports"),
    path("<int:vuln_id>", views.vulnerability, name="vulnerability"),
    path("AddNew", views.Add_new, name="AddNew"),
    path("Update/<str:vuln_id>/", views.updatevuln, name="Update"),
    path("Delete/<str:vuln_id>/", views.Delete, name="Delete"),
    path("Awaiting", views.Awaiting, name="Awaiting"),
    path("Escalated", views.Escalated, name="Escalated"),
    path("searchresults", views.searchresults, name="searchresults"),
    path("searchreference", views.searchreference, name="searchreference")
]
