from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_error/', views.signup, name='signup_error'),
    path('login/', views.login, name='login'),
    
    path('', views.main, name='main'),
    
    path('logout/', views.logout, name='logout'),
    path('introduce/', views.introduce, name='introduce'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    
    
]  