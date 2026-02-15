
from django.contrib import admin
from django.urls import path
from  productmanager.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('categoryPage/',categoryPage,name='categoryPage'),
    path('categoryEdit/<int:id>/',categoryEdit,name='categoryEdit'),
    path('categoryDelete/<int:id>/',categoryDelete,name='categoryDelete'),
    path('Productlist/',Productlist,name='Productlist'),
    path('ProductAdd/',ProductAdd,name='ProductAdd'),
    path('ProductEdit/<int:id>/',ProductEdit,name='ProductEdit'),
    path('ProductDelete/<int:id>/',ProductDelete,name='ProductDelete'),
    path('Orderlist/',Orderlist,name='Orderlist'),
    path('OrderAdd/',OrderAdd,name='OrderAdd'),
    path('OrderEdit/<int:id>/',OrderEdit,name='OrderEdit'),
    path('OrderDelete/<int:id>/',OrderDelete,name='OrderDelete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
