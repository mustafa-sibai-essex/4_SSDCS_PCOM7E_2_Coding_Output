from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.PublicUser)
admin.site.register(models.VulnerabilitiesOP)