from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    ROLES=[
        ('Job_Seeker','Job_Seeker'),
        ('Recruiter','Recruiter'),
    ]
    roles=models.CharField(choices=ROLES,max_length=100,null=True)

    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user=models.OneToOneField(UserModel,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=200,null=True)
    resume=models.FileField(upload_to='file/',null=True)

    def __str__(self):
        return self.user

class JobModel(models.Model):
    titel=models.CharField(max_length=100,null=True)
    company_name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    salary=models.IntegerField(null=True)
    location=models.CharField(max_length=200,null=True)
    posted_by=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titel
    
class ApplicationModel(models.Model):
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    applicant=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    cover_letter=models.FileField(upload_to='file/',null=True)
    applied_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job