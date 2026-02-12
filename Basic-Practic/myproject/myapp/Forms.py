from django import forms
from myapp.models import*

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        exclude = ['stock','total_amount']