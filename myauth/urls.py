from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'myauth'

urlpatterns = [
    #path('login/', login_view, name = 'login')
    path('login/',LoginView.as_view(template_name = 'myauth/login.html', redirect_authenticated_user = True), name= 'login'),
    path('logout/', views.logoutView, name = 'logout'),
    path('cookie/get/', views.get_cookie_view, name = 'cookie-get'),
    path('foo-bar/', views.FooBarView.as_view(), name = 'foo-bar'),
    path('profile/edit/<str:slug>/', views.AboutMeViewUpdate.as_view(), name='profileedit'),
    path('profile/<str:slug>/', views.AboutMeView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register')
]


