from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    """Extends the User model to add an IP address"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_addresses = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username
