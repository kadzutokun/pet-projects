from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'myauth'

urlpatterns = [
    #path('login/', login_view, name = 'login')
    path('login/',LoginView.as_view(template_name = 'myauth/login.html', redirect_authenticated_user = True), name= 'login'),
    path('logout/', views.logoutView, name = 'logout'),
    path('profile/<int:pk>', views.AboutMeView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register')
]


