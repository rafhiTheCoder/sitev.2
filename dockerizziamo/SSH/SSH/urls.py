"""
URL configuration for SSH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from register import views as register
from myapp import views as site
from API import views as API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register.register,name="register"),
    path('',site.home,name="home"),
    path("",include("myapp.urls")),
    path("dashboard/",site.dashboard,name="dashboard"),
    path("",include("django.contrib.auth.urls")),
    path("about/",site.about,name="about"),
    path("serre/",site.serre,name="serre"),
    path('serre/<int:serra_id>/delete/', site.delete_serra, name='delete_serra'),
    path('api/users/register/', API.RegisterUser.as_view(), name='register_user'),
    path('api/users/<str:username>/serre/add/', API.add_user_serra, name='add_user_serra'),
    path('api/users/<str:username>/', API.get_user_password, name='get_user_password'),
    path('api/users/<str:username>/serre/', API.get_user_serre, name='get_user_serre'),
    path('api/users/<str:username>/serre/<str:serra_code>/', API.delete_user_serra, name='delete_user_serra'),
    
    
]
