from django.urls import path

from . import views

app_name='blogpost'

urlpatterns = [
	path('',views.home,name='home'),
    path('cate/<str:cats>/',views.categories,name='categories'),
    path('subscribenow',views.subscribenow,name='subscribenow'),
    path('addblog',views.addblog,name='addblog'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('<int:pk>/',views.details,name='details'),
]
