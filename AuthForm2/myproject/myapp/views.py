from django.shortcuts import render,redirect
from myapp.models import*
from myapp.forms import*
from django.contrib.auth import login
# Create your views here.

def signup(r):
    if r.method=="POST":
        form = SignupFrom(r.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        form = SignupFrom()
    context={
        'form':form
    }
    return render (r,'signup.html',context)

def signin(r):
    if r.method=="POST":
        form = signinFrom(r,r.POST)
        if form.is_valid():
            user = form.get_user()
            login (r,user)
            return redirect('home')
        form = signinFrom()
    context={
        'form':form
    }
    return render (r,'signin.html',context)

def home(r):
    return render (r,'home.html')