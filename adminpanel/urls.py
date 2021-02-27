from django.urls import path
from adminpanel import views


urlpatterns = [
    path('', views.adminlogin, name = 'adminlogin'),
    path('home', views.adminhome, name = 'adminhome'),
    path('logout', views.adminlogout, name = 'adminlogout'),
    path('create/', views.adminadd, name ='adminadd'),
    path('search/', views.adminsearch, name ='adminsearch'),
    path('update/<int:pk>/', views.adminupdate, name='adminupdate'),
    path('delete/<int:pk>/', views.admindelete, name = 'admindelete'),


]