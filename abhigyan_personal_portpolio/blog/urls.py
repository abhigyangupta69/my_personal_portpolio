from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

app_name='blog'


urlpatterns = [
    path('',views.home_blog,name='home_blog'),
    path('<int:blog_id>/',views.details,name='details'),
    ]