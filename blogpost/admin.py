from django.contrib import admin

# Register your models here.
from .models import Post,Category,Comment,Subscribe
# Register your models here.

admin.site.register([Post,Category,Comment,Subscribe])
# admin.site.register(Category)
# admin.site.register(Comment)