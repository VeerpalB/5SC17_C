from django.urls import path
from . import views



urlpatterns = [
    path('', views.login, name='root_redirect'),
    path('user/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('progress/', views.progress_view, name='progress_name'),
    path('help/', views.help, name='help'),
    path('logout/', views.logout_view, name='logout'),
    path('voting/', views.voting, name='voting'),
    path('session/', views.session, name='session'),
    path('login/', views.login, name='login'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    path('forgotten_password_confirmation/', views.forgotten_password_confirmation, name='forgotten_password_confirmation'),
    path('signup/', views.signup, name='signup'),
    path('overview/home/', views.overview_home, name='overview_home'),
    path('department/overview', views.department_overview, name='department_overview'),
    path('overview/team', views.team_overview, name='team_overview'),
    path('dashboard/', views.dashboard, name='dashboard'),
  
   


    path('navbar/', views.navbar),
    path('welcome/', views.welcome_page, name='welcome'), #author : Nadia Islam
    path('department-overview/', views.dept_overview, name='department_overview'),
    path('senior/team-overview/', views.senior_team_overview, name='senior_team_overview'),

]
