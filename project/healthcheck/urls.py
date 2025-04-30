
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
    path('profile', views.profile, name='profile_name'),
    path('progress', views.progress, name='progress_name'),
    path('help', views.help, name='help_name'),
    path('logout', views.logout, name='logout_name'),
    path('voting', views.voting, name='voting_name'),
    path('editsession', views.edit, name='edit_name'),


    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    path('forgotten_password_confirmation/', views.forgotten_password_confirmation, name='forgotten_password_confirmation'),




    path('navbar/', views.navbar),
  
]
