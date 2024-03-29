from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
            return render(request, 'signup_error.html')
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                last_name=request.POST['last_name'],
                first_name=request.POST['first_name'],
            )
            auth.login(request, user)

            return redirect('main')
          

    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
             auth.login(request, user)
             return redirect('main')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
            
    else:
        return render(request, "login.html")
    
def main(request):
    return render(request, 'main.html')

def introduce(request):
    return render(request, 'introduce.html')

def logout(request):
    auth.logout(request)
    redirect('main')
    return render(request,'login.html')
    
