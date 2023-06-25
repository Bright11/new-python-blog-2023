from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
# category model
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name
        

# post model
class Post(models.Model):
    title=models.TextField(max_length=100)
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    post=models.TextField()
    image=models.ImageField(upload_to='post_images',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.created_by.username
    
# comment
class Comment(models.Model):
    post_id=models.ForeignKey(Post,related_name='posts',on_delete=models.CASCADE)
    comment=models.TextField()
    user=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    


# subscrips
class Subscribe(models.Model):
    newslatter=models.EmailField()
    def __str__(self):
        return self.newslatter