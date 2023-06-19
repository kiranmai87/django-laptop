"""
URL configuration for laptops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings

from lapapp.views import home,contact,login_user,logout_user,register,hp,lenovo,asus,acer,realme,msi,smarton

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",login_user,name="login"),
    path("home/",home,name="home"),
    path("contact/",contact,name="contact"),
    path("logout/",logout_user,name="logout"),
    path("register/",register,name="register"),
    path("hp/",hp,name="hp"),
    path("lenovo/",lenovo,name="lenovo"),
    path("asus/",asus,name="asus"),
    path("acer/",acer,name="acer"),
    path("realme/",realme,name="realme"),
    path("msi/",msi,name="msi"),
    path("smarton/",smarton,name="smarton"),
 
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
