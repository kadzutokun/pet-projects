from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.urls import reverse
# Create your views here.

def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/shop/')
        
        return render(request, 'myauth/login.html')
    
    username = request.POST['username']
    password = request.POST['password']


    user = authenticate(request, username = username, password = password)
    
    if user is not None:
        login(request,user)
        return redirect('/shop/')
    
    return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})

def logoutView(request:HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))

