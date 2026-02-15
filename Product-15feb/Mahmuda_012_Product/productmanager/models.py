from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    ROLL=[
        ('Admin','Admin'),
        ('Seller','Seller'),
        ('Customer','Customer'),
    ]
    full_name=models.CharField(max_length=100,null=True)
    role=models.CharField(choices=ROLL,max_length=100,null=True)

    def __str__(self):
        return str(self.full_name)
    
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
class ProductModel(models.Model):
    seller=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=100,null=True)
    product_description=models.TextField(null=True)
    product_image=models.ImageField(upload_to='image/',null=True)
    price=models.IntegerField(null=True)
    stock_quantity=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
class OrderModel(models.Model):
    STATUS=[
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Cancelled','Cancelled'),
    ]
    customer=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    order_status=models.CharField(choices=STATUS,max_length=100,null=True)
    ordered_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.product.product_name}"