"""Contains the models used in thr app. Each class is a table in the database."""

from django.db import models


class PublicUser(models.Model):
    """A table to store the data of a public user."""
    user_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="Anonymous")
    last_name = models.CharField(max_length=50, default="User")
    email = models.EmailField(max_length=100, default="No email")
    remarks = models.TextField(blank=True, max_length=1000)


class Vulnerabilities(models.Model):
    """A table to store the vulnerability data reported by the user."""
    AwaitingApproval = 'Awaiting Approval'
    Assigned = 'Assigned'
    Rejected = "Rejected"
    Fixed = 'Fixed'
    Escalated = 'Escalated'
    Ua = 'Unassigned'
    G_a = 'General Affairs'
    Agri = "Agriculture, Nature and Food Quality"
    Def = 'Defence'
    Econ = 'Economic Affairs'
    Edu = 'Education'
    Fin = 'Finance'
    For_aff = 'Foreign Affairs'
    Health = 'Health, Welfare and sport'
    Infra = 'Infrastructure'
    Int = 'Interior and Kingdom relations'
    Justice = 'Justice and Security'
    Soc = 'Social Affairs and Employment'
    Esc = 'Escalation Team'

    Status_choices = [
        (AwaitingApproval, 'Awaiting approval'),
        (Assigned, 'Assigned'),
        (Rejected, 'Rejected'),
        (Fixed, 'Fixed'),
        (Escalated, 'Escalated'),
    ]

    dept_choices = [
        (Ua, 'Unassigned'),
        (G_a, 'General Affairs'),
        (Agri, "Agriculture, Nature and Food Quality"),
        (Def, 'Defence'),
        (Econ, 'Economic Affairs'),
        (Edu, 'Education'),
        (Fin, 'Finance'),
        (For_aff, 'Foreign Affairs'),
        (Health, 'Health, Welfare and sport'),
        (Infra, 'Infrastructure'),
        (Int, 'Interior and Kingdom relations'),
        (Justice, 'Justice and Security'),
        (Soc, 'Social Affairs and Employment'),
        (Esc, 'Escalation Team'),
    ]

    vul_no = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, choices=Status_choices, default=AwaitingApproval)
    assigned_to = models.CharField(max_length=100, choices=dept_choices, default=Ua, null=True)
    reported_by = models.ForeignKey(PublicUser, on_delete=models.DO_NOTHING, null=True)
    vulnerable_website = models.URLField(max_length=200)
    date_time = models.DateTimeField(max_length=50)
    description = models.TextField(max_length=1000)
    replicate = models.TextField(max_length=1000)
    exploit_code = models.TextField(blank=True, max_length=2000)
    potential_fix = models.TextField(blank=True, max_length=1000)
    video = models.URLField(blank=True, max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
