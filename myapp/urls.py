from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.register, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('logout', views.userlogout, name='logout')
    
]