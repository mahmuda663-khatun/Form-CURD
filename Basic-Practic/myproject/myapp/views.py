from django.shortcuts import render,redirect
from myapp.models import*
from myapp.Forms import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from decimal import Decimal
from django.contrib import messages 
# Create your views here.

def home(r):
    return render(r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        email=r.POST.get('email')
        password=r.POST.get('password')
        role=r.POST.get('role')
        confirm_password=r.POST.get('confirm_password')

        user_exits=UserModel.objects.filter(username=username).exists()

        if user_exits:
            messages.warning(r,'user already exit')
            return redirect('signup')
        
        if confirm_password==password:
           UserModel.objects.create_user(
                username=username,
                email=email,
                password= confirm_password,
                role=role
            )
           return redirect ('signin')  
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(username=username,password=password)

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

def ChangePass(r):
    current_user=r.user

    if r.method=="POST":
        current_password=r.POST.get('current_password')
        new_password=r.POST.get('new_password')
        confirm_password=r.POST.get('confirm_password')

        if check_password(current_password,current_user.password):

            if confirm_password==new_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect('home')

    return render (r,'ChangePass.html')

def CategoryPage(r):
    C_data=CategoryModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        CategoryModel.objects.create(
            name=name,
        )
    context={
        'C_data':C_data
    }
    return render (r,'CategoryPage.html',context)

def CategoryEdit(r,id):
    E_data=CategoryModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')

        E_data.name=name
        E_data.save()
        return redirect('CategoryPage')
    context={
        'C_data':E_data
    }
    return render (r,'CategoryEdit.html',context)

def CategoryDelete(r,id):
    CategoryModel.objects.get(id=id).delete()
    return redirect ('CategoryPage')

def Productlist(r):
    p_data=ProductModel.objects.all()
    context={
        'p_data':p_data
    }
    return render (r,'Productlist.html',context)

def ProductAdd(r):
    if r.method=="POST":
        P_data=ProductForm(r.POST)

        if P_data.is_valid():
            data=P_data.save(commit=False)
            data.stock = 'Available'
            data.total_amount = data.unit_price * data.qty
            data.save()
            return redirect('Productlist')
    else:
        P_data=ProductForm()

    context={
        'P_data':P_data
    }
    return render (r,'ProductAdd.html',context)

def ProductEdit(r,id):
    E_data=ProductModel.objects.get(id=id)
    if r.method=="POST":
        P_data=ProductForm(r.POST, instance=E_data)

        if P_data.is_valid():
            data=P_data.save(commit=False)
            data.stock = 'Available'
            data.total_amount = data.unit_price * data.qty
            data.save()
            return redirect('Productlist')
    else:
        P_data=ProductForm(instance=E_data)

    context={
        'P_data':P_data
    }
    return render (r,'ProductAdd.html',context)


def ProductDelete(r,id):
    ProductModel.objects.get(id=id).delete()
    return redirect ('Productlist')