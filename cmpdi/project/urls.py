from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.Contact, name='contact'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('account', views.account, name='account'),


    path('create/', views.random_detail_create, name='random_detail_create'),
]
