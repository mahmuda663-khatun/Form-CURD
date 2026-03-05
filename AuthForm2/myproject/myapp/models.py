from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AuthUserModel(AbstractUser):
    USER_TYPE = [
        ('teacher','teacher'),
        ('student','student'),
    ]

    display_name= models.CharField(max_length=50,null=True)
    role= models.CharField(choices=USER_TYPE, max_length=50,null=True)