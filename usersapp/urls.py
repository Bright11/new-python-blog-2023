from django.urls import path
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import logout
from . import views
from .forms import LoginForm
app_name='usersapp'
# https://magspot-simple.blogspot.com/
urlpatterns = [
	path('',views.signup,name='signup'),
    path('signin/',auth_views.LoginView.as_view(template_name='pages/signin.html',authentication_form=LoginForm),name='signin'),
    path('userlogout/',views.userlogout,name='userlogout'),
]
