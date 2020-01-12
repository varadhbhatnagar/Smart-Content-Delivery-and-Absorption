"""SCAD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.UserSignupFormView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('system_control/', views.system_control, name='system_control'),
    path('records/', views.records, name='records'),
    path('visualize/', views.visualize, name='visualize'),
    path('', views.home, name='home'),
    path('text-content/', views.text_content, name='text_content')

]
