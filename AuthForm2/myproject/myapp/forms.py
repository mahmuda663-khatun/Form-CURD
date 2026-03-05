from django import forms
from myapp.models import*
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupFrom(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = ['username','display_name','role','password1','password2']

class signinFrom(AuthenticationForm):
    pass