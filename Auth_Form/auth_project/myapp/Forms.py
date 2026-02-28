from django import forms
from myapp.models import*
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegisterFrom(UserCreationForm):
    class Meta:
        model = AuthUserModel
        
        fields = ['username', 'display_name', 'role', 'email', 'password1', 'password2']

class signinForm(AuthenticationForm):
    pass