from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user=user)
            return redirect('home')
        
    return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(email=email).exists():
             return redirect('register')
        elif User.objects.filter(username=username).exists():
             return redirect('register')
        elif password1 != password2:
            return redirect('register')
        else:

            new_user = User(username=username, email=email)
            new_user.set_password(password1)
            new_user.save()

            return redirect('login')
        
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('login')