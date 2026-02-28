
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('home/',home,name='home'),
]