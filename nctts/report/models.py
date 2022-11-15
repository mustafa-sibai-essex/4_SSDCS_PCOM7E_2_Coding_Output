from django.db import models


class PublicUser(models.Model):
    user_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Vulnerability(models.Model):
    vulnerability_no = models.AutoField(primary_key=True)
    reported_by = models.EmailField(max_length=100)
    vulnerable_website = models.URLField(max_length=200)
    date_time = models.DateTimeField(max_length=50)
    description = models.TextField(max_length=1000)
    replicate = models.TextField(max_length=1000)
    exploit_code = models.TextField(max_length=2000)
    potential_fix = models.TextField(max_length=1000)
    video = models.URLField(blank=True, max_length=200)


