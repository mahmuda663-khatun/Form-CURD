
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
]
