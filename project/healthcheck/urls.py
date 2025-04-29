
from django.urls import path
from . import views



urlpatterns = [
    path('user', views.home, name='home_name'),
    path('profile/', views.profile, name='profile_name'),
    path('progress/', views.progress, name='progress_name'),
    path('help/', views.help, name='help_name'),
    path('logout/', views.logout, name='logout_name'),
    path('voting/', views.voting, name='voting_name'),
    path('login/', views.login, name='login_name'),
    path('signup/', views.signup, name='signup_name'),


    path('navbar/', views.navbar),
    path('welcome/', views.welcome_page, name='welcome'), #Nadia
    path('department-overview/', views.dept_overview, name='department_overview'),
]
