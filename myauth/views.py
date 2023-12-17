from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
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
    # template_name = 'myauth/logout.html'
    logout(request)
    return redirect(reverse('myauth:login'))


class AboutMeView(TemplateView):
    template_name = 'myauth/user_info.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:profile')
    def form_valid(self, form): # Переопределение form_valid, дабы после регистрации осуществлять автоматический вход на аккаунт
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')


        user = authenticate(self.request, username=username, password = password)
        login(self.request, user)
        return response



