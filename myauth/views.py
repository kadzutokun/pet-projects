from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group,Permission
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.views import View
from . import models
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
        

class AboutMeView(DetailView):
    model = models.Profile
    template_name = 'myauth/user_info.html'
    context_object_name = 'profile'
 

class AboutMeViewUpdate(UpdateView):
    template_name = 'myauth/user_info_edit.html'
    model = models.Profile
    fields = ('university','slug')
    success_url = reverse_lazy('myauth:profileedit')
    def get_success_url(self):
        return reverse('myauth:profile', kwargs={'slug': self.object.slug})


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:profile')

    def form_valid(self, form): # Переопределение form_valid, дабы после регистрации осуществлять автоматический вход на аккаунт
        response = super().form_valid(form)
        models.Profile.objects.create(user = self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password = password)
        login(self.request, user)
        return response


def get_cookie_view(request: HttpRequest):
    value = request.COOKIES.get("fizz", 'default value')
    return HttpResponse(f'Cookie value = {value}')

class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({'foo': 'bar', 'spam': 'eggs'})

