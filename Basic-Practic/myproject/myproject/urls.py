
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('ChangePass/',ChangePass,name='ChangePass'),
    path('CategoryPage/',CategoryPage,name='CategoryPage'),
    path('CategoryEdit/<int:id>/',CategoryEdit,name='CategoryEdit'),
    path('CategoryDelete/<int:id>/',CategoryDelete,name='CategoryDelete'),
    path('Productlist/',Productlist,name='Productlist'),
    path('ProductAdd/',ProductAdd,name='ProductAdd'),
    path('ProductEdit/<int:id>/',ProductEdit,name='ProductEdit'),
    path('ProductDelete/<int:id>/',ProductDelete,name='ProductDelete'),
]
