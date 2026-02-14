from django.shortcuts import render,redirect
from myapp.models import*
from myapp.Form import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.

def home(r):
    return render (r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        roles=r.POST.get('roles')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        exits=UserModel.objects.filter(username=username).exists()

        if exits:
            messages.warning(r,'username already exit')
            return redirect('signup')

        if confirm_password==password:
            UserModel.objects.create_user(
                username=username,
                roles=roles,
                password=password,
            )
            return redirect('signin') 
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)

        if user:
            login(r,user)
            messages.success(r,'successfully login')
            return redirect('home')
        else:
            messages.warning(r,'invalid')
            return redirect('signin')
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')

    
def Chengepass(r):
    current_user=r.user
    if r.method=="POST":
        current_password=r.POST.get('current_password')
        new_password=r.POST.get('new_password')
        confirm_password=r.POST.get('confirm_password')

        if check_password(current_password,current_user.password):

            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect('home')
    return render(r,'Chengepass.html')

def Profilelist(r):
    P_data=ProfileModel.objects.all()

    context={
        'P_data':P_data
    }
    return render (r,'Profilelist.html',context)

def ProfileAdd(r):
    if r.method=="POST":
        skills=r.POST.get('skills')
        experience=r.POST.get('experience')
        resume=r.FILES.get('resume')
        
        ProfileModel.objects.create(
            user=r.user,
           skills=skills,
           experience=experience,
           resume=resume,
        )
        return redirect('Profilelist')
    return render (r,'ProfileAdd.html')

def Profiledit(r,id):
    E_data=ProfileModel.objects.get(id=id)
    if r.method=="POST":
        skills=r.POST.get('skills')
        experience=r.POST.get('experience')
        resume=r.FILES.get('resume')

        E_data.skills=skills,
        E_data.experience=experience,
        E_data.resume=resume,
        E_data.save()
        return redirect ('Profilelist')
    context={
        'E_data':E_data
    }
    return render (r,'Profileledit.html',context)

def ProfileDelete(r,id):
    ProfileModel.objects.get(id=id).delete()
    return redirect ('Profilelist')

def Joblist(r):
    j_data=JobModel.objects.all()
    context={
        'j_data':j_data
    }
    return render (r,'Joblist.html',context)

def JobAdd(r):
    if r.method == 'POST':
       job_data = JobForm(r.POST)
       if job_data.is_valid():
           job = job_data.save(commit=False)
           job.posted_by=r.user
           job.save()
           return redirect('Joblist')
       
    job_data = JobForm()
    context={
        'job_data':job_data
    }
    return render (r,'JobAdd.html',context)

def JobEdit(r,id):
    E_data=JobModel.objects.get(id=id)
    if r.method == 'POST':
       job_data = JobForm(r.POST,instance=E_data)
       if job_data.is_valid():
           job = job_data.save(commit=False)
           job.posted_by=r.user
           job.save()
           return redirect('Joblist')
       
    job_data = JobForm(instance=E_data)
    context={
        'job_data':job_data
    }
    return render (r,'JobAdd.html',context)

def JobDelete(r,id):
    JobModel.objects.get(id=id).delete()
    return redirect ('Joblist')