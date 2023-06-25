from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SingupForm(UserCreationForm):
    class Meta:
        model=User 
        fields=('username','email','password1','password2')
        username=forms.CharField(label='search',widget=forms.TextInput(attrs={'placeholder': 'User name'}))
        email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
        password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
        
       

# login
class LoginForm(AuthenticationForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))