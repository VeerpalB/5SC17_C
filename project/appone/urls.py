
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home_name'),  
    path('blist/<str:id>', views.blist, name='blist_name'),
    path('navbar/', views.navbar),
]