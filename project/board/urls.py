from django.contrib import admin
from django.urls import path
from . import views  # 해당 앱의 뷰를 불러온다.


urlpatterns = [
    path('list/', views.list, name='list'),  # list를 보여주는 뷰와 연결한다.
    path('create/', views.create, name='create'),#글의 작성화면
    path('posting/<int:pk>/', views.posting, name='posting'),
    path('participate/', views.participate, name='participate'),
    path('login/', views.login, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage_edit/', views.mypage_edit, name='mypage_edit'),
    path('like/<int:blog_id>/', views.likes, name="likes"),
    path('summernote/', views.summernote, name ='summernote'),
]