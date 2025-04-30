from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),
    path('profile/', views.profile, name='profile_name'),
    path('progress', views.progress, name='progress_name'),
    path('help', views.help, name='help_name'),
    path('logout', views.logout, name='logout_name'),
    path('voting', views.voting, name='voting_name'),

    path('session', views.edit, name='sessions_name'),


    path('login/', views.login, name='login'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    path('forgotten_password_confirmation/', views.forgotten_password_confirmation, name='forgotten_password_confirmation'),
    path('signup/', views.signup, name='signup'),
    path('overview/home', views.overview_home, name='overview_home'),
    path('department/overview', views.department_overview, name='department_overview'),
    path('overview/team', views.team_overview, name='team_overview'),
    path('dashboard/', views.dashboard, name='dashboard'),
   


    path('navbar/', views.navbar),
  
]
