
from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),
    path('profile/', views.profile, name='profile_name'),
<<<<<<< HEAD
    path('progress/', views.progress, name='progress_name'),
    path('help/', views.help, name='help_name'),
    path('logout/', views.logout, name='logout_name'),
    path('voting/', views.voting, name='voting_name'),
    path('login/', views.login, name='login_name'),
    path('signup/', views.signup, name='signup_name'),
=======
    path('progress', views.progress, name='progress_name'),
    path('help', views.help, name='help_name'),
    path('logout', views.logout, name='logout_name'),
    path('voting', views.voting, name='voting_name'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgottenpassword/', views.forgottenpassword, name='forgottenpassword'),
    path('signup/', views.signup, name='signup'),
    path('overview/home', views.overview_home, name='overview_home'),
    path('department/overview', views.department_overview, name='department_overview'),
    path('overview/team', views.team_overview, name='team_overview'),
 
   
>>>>>>> 514e73cac4ef398b1b035e029ece1dbde4cdb73f


    path('navbar/', views.navbar),
    path('welcome/', views.welcome_page, name='welcome'), #Nadia
    path('department-overview/', views.dept_overview, name='department_overview'),
    path('senior/team-overview/', views.senior_team_overview, name='senior_team_overview'),

]
