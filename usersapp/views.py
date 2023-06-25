from django.shortcuts import render,redirect
from .forms import SingupForm, LoginForm
# Create your views here.
from django.contrib.auth import logout
from django.contrib import messages
#from django.http import HttpResponseRedirect

def signup(request):
    if request.method=='POST':
       
        signupforms=SingupForm(request.POST)
       
        if signupforms.is_valid():
            #print('hi yes pass v')
            signupforms.save()
            print('saved')
            return redirect('usersapp:index')
    else:
        signupforms=SingupForm()
    return render(request,'pages/signup.html',{
        'signupforms':signupforms,'title':'Singup'
	})

def userlogout(request):
    logout(request)
    messages.success(request,('you are logout'))
    #return  redirect('usersapp:index')
    return redirect('usersapp:signup')