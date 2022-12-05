"""We register our models here so that we can see and manage them on the admin backend."""

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.PublicUser)
admin.site.register(models.Vulnerabilities)
