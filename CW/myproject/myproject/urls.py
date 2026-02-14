
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('Chengepass/',Chengepass,name='Chengepass'),
    path('Profilelist/',Profilelist,name='Profilelist'),
    path('ProfileAdd/',ProfileAdd,name='ProfileAdd'),
    path('Profiledit/<int:id>/',Profiledit,name='Profiledit'),
    path('ProfileDelete/<int:id>/',ProfileDelete,name='ProfileDelete'),
    path('Joblist/',Joblist,name='Joblist'),
    path('JobAdd/',JobAdd,name='JobAdd'),
    path('JobEdit/<int:id>/',JobEdit,name='JobEdit'),
    path('JobDelete/<int:id>/',JobDelete,name='JobDelete'),
    path('Applicationlist/',Applicationlist,name='Applicationlist'),
    path('ApplicationAdd/',ApplicationAdd,name='ApplicationAdd'),
    path('ApplicationEdit/<int:id>/',ApplicationEdit,name='ApplicationEdit'),
    path('ApplicationDelete/<int:id>/',ApplicationDelete,name='ApplicationDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
