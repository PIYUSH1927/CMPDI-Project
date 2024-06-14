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
    path('billview', views.billview, name='billview'),
    path('create/', views.bills_detail_create, name='bills_detail_create'),
    path('update_payment_status', views.update_payment_status, name='update_payment_status'),
    path('adminview', views.adminview, name='adminview'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('update_status', views.update_status, name='update_status'),
    path('filter_bills/', views.filter_bills, name='filter_bills'),
]


