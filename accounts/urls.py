from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('register/',views.register,name='register'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('login/',views.login_here,name='login'),
    path('logout-user/',views.logout_user,name='logout_user'),
    path('customer/<str:pk_id>/',views.customers,name='customers'),
    path('create-order/<str:pk>/',views.create_order,name='create_order'),
    path('update-order/<str:pk>/',views.update_order,name='update_order'),
    path('delete-order/<str:pk>/',views.delete_order,name='delete_order'),
]