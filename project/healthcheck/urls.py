
from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),
    path('profile/', views.profile, name='profile_name'),
    path('progress/', views.progress, name='progress_name'),
    path('help/', views.help, name='help_name'),
    path('logout/', views.logout, name='logout_name'),
    path('voting/', views.voting, name='voting_name'),
    path('session/', views.session, name='session_name'),
    path('dashboard/', views.dashboard, name='dashboard_name'),
    path('navbar/', views.navbar),
  
]