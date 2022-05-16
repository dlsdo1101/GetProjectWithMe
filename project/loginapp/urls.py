from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home2, name='home2'),
    path('home/', views.home, name='home'),
    
    path('logout/', views.logout, name='logout'),

]  