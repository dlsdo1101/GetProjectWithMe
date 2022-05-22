from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
    path('', views.main, name='main'),
    
    path('logout/', views.logout, name='logout'),
    path('introduce/', views.introduce, name='introduce')

]  