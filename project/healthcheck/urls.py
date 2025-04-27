
from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),
    path('profile/', views.profile, name='profile_name'),
    path('progress/', views.progress, name='progress_name'),
    path('help/', views.help, name='help_name'),
    path('logout/', views.logout, name='logout_name'),
    path('voting/', views.voting, name='voting_name'),
    path('login/', views.login, name='login_name')



    path('navbar/', views.navbar),
  
]