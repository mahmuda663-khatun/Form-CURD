from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    ROLE=[
        ('Admin','Admin'),
        ('User','User')
    ]
    role=models.CharField(choices=ROLE,max_length=10,null=True)
    def __str__(self):
        return self.username
    
class CategoryModel(models.Model):
    name=models.CharField(null=True)
    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    STOK=[
        ('Available','Available'),
        ('Stock_Out','Stock_Out')
    ]
    name=models.CharField(null=True)
    unit_price=models.DecimalField(decimal_places=4,max_digits=10,null=True)
    qty=models.IntegerField(null=True)
    total_amount=models.DecimalField(decimal_places=4,max_digits=10,null=True)
    stock=models.CharField(choices=STOK,max_length=10,null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name

