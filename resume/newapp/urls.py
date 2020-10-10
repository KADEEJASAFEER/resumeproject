"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from newapp.views import CreateResume,register,loginPage,logoutPage,index,viewResume,editResume,deleteResume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createresume',CreateResume,name="createresume"),
    path('register',register,name="register"),
    path('',loginPage,name="loginpage"),
    path('logoutpage',logoutPage,name="logoutpage"),
    path('index',index,name="index"),
    path('viewresume',viewResume,name="viewresume"),
    path('editresume/<int:pk>',editResume,name="editresume"),
    path('deleteresume/<int:pk>',deleteResume,name="deleteresume")

 ]
