from django.shortcuts import render,redirect
from productmanager.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from productmanager.Form import*
# Create your views here.


def home(r):
    return render(r,'home.html')

def signup(r):
    if r.method=="POST":
        full_name=r.POST.get('full_name')
        username=r.POST.get('username')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')
        role=r.POST.get('role')

        user_exit=CustomUserModel.objects.filter(username=username).exists()
        
        if user_exit:
            messages.warning(r,"user already exits")
            return redirect('signin')

        if confirm_password==password:
            CustomUserModel.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
                role=role
            )
            return redirect ('signin')
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)
        if user:
            login(r,user)
            messages.success(r,'Successfuly Login')
            return redirect ('home')
        else:
          messages.warning(r,'invalid')
          return redirect('signin')  
        
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')

def categoryPage(r):
    C_data=CategoryModel.objects.all()
    if r.method=="POST":
        category_name=r.POST.get('category_name')
        description=r.POST.get('description')
        
        CategoryModel.objects.create(
            category_name=category_name,
            description=description,
        )
    context={
        'C_data':C_data
    }
    return render(r,'categoryPage.html',context)

def categoryEdit(r,id):
    E_data=CategoryModel.objects.get(id=id)
    if r.method=="POST":
        category_name=r.POST.get('category_name')
        description=r.POST.get('description')

        E_data.category_name=category_name,
        E_data.description=description,
        E_data.save()
        return redirect ('categoryPage')
    context={
        'E_data':E_data
    }
    return render(r,'categoryEdit.html',context)

def categoryDelete(r,id):
    CategoryModel.objects.get(id=id).delete()
    return redirect("categoryPage")

def Productlist(r):
    P_data=ProductModel.objects.all()
    context={
        'P_data':P_data
    }
    return render (r,'Productlist.html',context)

def ProductAdd(r):
    if r.method=="POST":
        product=ProductForm(r.POST,r.FILES)

        if product.is_valid():
            product.save()
            return redirect('Productlist')

    product=ProductForm() 
    context={
       'product':product
    }
    return render (r,'ProductAdd.html',context)

def ProductEdit(r,id):
    p_data=ProductModel.objects.get(id=id)
    if r.method=="POST":
        product=ProductForm(r.POST,r.FILES,instance=p_data)

        if product.is_valid():
            product.save()
            return redirect('Productlist')

    product=ProductForm(instance=p_data) 
    context={
       'product':product
    }
    return render (r,'ProductAdd.html',context)

def ProductDelete(r,id):
    ProductModel.objects.get(id=id).delete()
    return render ('Productlist')

def Orderlist(r):
    O_data=ProductModel.objects.all()
    context={
        'O_data':O_data
    }
    return render (r,'Orderlist.html',context)

def OrderAdd(r):
    if r.method=="POST":
        Order=OrderForm(r.POST)

        if Order.is_valid():
            Order_data=Order.save(commit=False)
            Order_data.order_status = 'Pending'
            Order_data.total_price = Order_data.quantity * Order_data.product.price
            Order_data.save()
            return redirect('Orderlist')

    Order=OrderForm() 
    context={
       'Order':Order
    }
    return render (r,'OrderAdd.html',context)

def OrderEdit(r,id):
    E_data=OrderModel.objects.get(id=id)
    if r.method=="POST":
        Order=OrderForm(r.POST,instance=E_data)

        if Order.is_valid():
            Order_data=Order.save(commit=False)
            Order_data.order_status = 'Pending'
            Order_data.total_price = Order_data.quantity * Order_data.product.price
            Order_data.save()
            return redirect('Orderlist')

    Order=OrderForm(instance=E_data) 
    context={
       'Order':Order
    }
    return render(r,'OrderAdd.html',context)

def OrderDelete(r,id):
    OrderModel.objects.get(id=id).delete()
    return redirect('Orderlist')