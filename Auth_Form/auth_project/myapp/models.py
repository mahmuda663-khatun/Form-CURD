from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AuthUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin','Admin'),
        ('Staff','Staff'),
    ]
    display_name = models.CharField(max_length=100,null=True)
    role = models.CharField(choices=USER_TYPE, max_length=10, null=True)

    def __str__(self):
        return self.username
