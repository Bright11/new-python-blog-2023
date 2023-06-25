from django.shortcuts import render,redirect,get_object_or_404
from .forms import Addcategory,PostForm,NewslatterForm
from django.contrib.auth.decorators import login_required
from .models import Post,Category

# Create your views here.
def home(request):
    post=Post.objects.all()
    categories=Category.objects.all()
    subscribe=NewslatterForm()
    return render(request,'post/home.html',{
           'post':post,'title':'blog page','subscribe':subscribe,
           'categories':categories
	})


def addcategory(request):
        if request.method=="POST":
              categoryform=Addcategory(request.POST)
              if categoryform.is_valid():
                    categoryform.save()
                    return redirect('blogpost:addcategory')
        else:
                categoryform=Addcategory()
                return render(request,'admin/addcategory.html',{
              'title':'Add Category','categoryform':categoryform
	})
        
# code to add blogs
@login_required
def addblog(request):
      if request.method=="POST":
            
            postform=PostForm(request.POST, request.FILES)
            if postform.is_valid():
                  blog=postform.save(commit=False)
                  blog.created_by=request.user
                  blog.save()
                  return redirect('blogpost:addblog')
      else:
                postform=PostForm()
                return render(request,'post/addblog.html',{
            'title':'Add blog','postform':postform
	  })

# getting categories

def categories(request,cats):
       postcat=Post.objects.filter(category=cats)
       #print(postcat)
       return render(request,'post/categories.html',{
              'postcat':postcat,'title':'Category'
       })

# details page
def details(request,pk):
       getpost=get_object_or_404(Post,pk=pk)
       categories=Category.objects.all()
       print(getpost.id) 
       return render(request,'post/details.html',{
              'getpost':getpost,'categories':categories
       })
# subscription backend
def subscribenow(request):
       if request.method=="POST":
              subscribe=NewslatterForm(request.POST)
              if subscribe.is_valid():
                     subscribe.save()
                     return redirect('blogpost:home')