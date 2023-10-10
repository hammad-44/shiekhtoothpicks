from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('orderform',views.orderform, name='orderform'),
    path('order',views.order, name='order')
    
]
    