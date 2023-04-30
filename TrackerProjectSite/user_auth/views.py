from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import Registration_Form


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
                        
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
        })

def logout_user(request):
    logout(request)
    return render(request, 'authentication/logout.html')

def register_user(request):
    if request.method=='POST':
        registration_form = Registration_Form(request.POST) 
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('user_auth:show_user')
    else: 
        registration_form = Registration_Form()
    return render(request, 'authentication/user_registration.html', {'registration_form': registration_form})