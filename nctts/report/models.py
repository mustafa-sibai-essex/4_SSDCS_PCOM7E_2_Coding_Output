from django.db import models


class PublicUser(models.Model):
    user_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="Anonymous")
    last_name = models.CharField(max_length=50, default="User")
    email = models.EmailField(max_length=100, default="No email")
    remarks = models.TextField(blank=True, max_length=1000)


class Vulnerabilities(models.Model):
    vul_no = models.AutoField(primary_key=True)
    reported_by = models.ForeignKey(PublicUser, on_delete=models.DO_NOTHING, null=True)
    vulnerable_website = models.URLField(max_length=200)
    date_time = models.DateTimeField(max_length=50)
    description = models.TextField(max_length=1000)
    replicate = models.TextField(max_length=1000)
    exploit_code = models.TextField(blank=True, max_length=2000)
    potential_fix = models.TextField(blank=True, max_length=1000)
    video = models.URLField(blank=True, max_length=200)
