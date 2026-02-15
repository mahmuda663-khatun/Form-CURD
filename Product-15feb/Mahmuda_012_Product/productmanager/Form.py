from django import forms
from productmanager.models import*

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        exclude = ["order_status","total_price"]