"""This file contains the paths of the pages in the app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.report, name="report"),
    path("success", views.success, name="success"),
    path("delete_info", views.delete_info, name="delete_info"),
    path("delete_success", views.delete_success, name="delete_success"),
    path("view_vulnerabilities", views.view_vulnerabilities, name="view_vulnerabilities"),
    path("delete_error", views.delete_error, name="delete_error"),
]
