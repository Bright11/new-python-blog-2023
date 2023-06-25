from django import forms

from .models import Category,Post,Subscribe

class Addcategory(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)
        name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"category"}))


# post forms
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('category','post','title','image')
        title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Blog title'}))
        category=forms.CharField(widget=forms.Select(attrs={'Placeholder':'Select'}))
        post=forms.CharField(widget=forms.Textarea(attrs={'Placeholder':'Write your blog'}))
        image=forms.CharField(widget=forms.ImageField())



# subscribe

class NewslatterForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields=('newslatter',)
        newslatter=forms.CharField(widget=forms.EmailField)