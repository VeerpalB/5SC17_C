from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse




def home(request):
    return render(request, 'healthcheck/home.html')

def profile(request):           
    return render(request, 'healthcheck/profile.html')

def progress(request):
   
    return render(request, 'healthcheck/progress.html')
    

def help(request):
    return render(request, 'healthcheck/help.html')

def logout(request):
    return render(request, 'healthcheck/logout.html')

def voting(request):
    return render(request, 'healthcheck/voting.html')

def edit(request):
    return render(request, 'healthcheck/edit.html')


def session(request):
    return render(request, 'healthcheck/session.html')  

def dashboard(request):
    return render(request, 'healthcheck/dashboard.html')

def login(request):
    return render(request, "healthcheck/login.html")

def signup(request):
    return render(request, "healthcheck/signup.html")

def forgotten_password(request):
    return render(request, 'healthcheck/forgotten_password.html')

def forgotten_password_confirmation(request):
    return render(request, 'healthcheck/forgotten_password_confirmation.html')

def navbar(request):
      return render(request, 'healthcheck/navbar.html')

