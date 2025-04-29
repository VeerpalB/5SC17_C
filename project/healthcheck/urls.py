
from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),

    path('profile/', views.profile, name='profile'),
    path('progress/', views.progress, name='progress'),
    path('help/', views.help, name='help'),
    path('logout/', views.logout, name='logout'),
    path('voting/', views.voting, name='voting'),
    path('session/', views.session, name='session'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('help/', views.help, name='help'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    path('forgotten_password_confirmation/', views.forgotten_password_confirmation, name='forgotten_password_confirmation'),




    path('navbar/', views.navbar),
  
]
