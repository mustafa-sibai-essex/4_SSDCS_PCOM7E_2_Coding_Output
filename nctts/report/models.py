from django.db import models

class PublicUser(models.Model):
    user_no =  models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Vulnerability(models.Model):
    vulnerability_no = models.AutoField(primary_key=True)
    reported_by = models.ForeignKey('PublicUser', on_delete=models.CASCADE)
    vulnerable_website = models.URLField(max_length=200)
    date_time = models.DateTimeField(max_length=50)
    description = models.CharField(max_length=1000)
    replicate = models.CharField(max_length=1000)
    exploit_code = models.CharField(max_length=2000)
    potential_fix = models.CharField(max_length=1000)

