from django import forms
from myapp.models import*

class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'
        exclude= ['posted_by','created_at']