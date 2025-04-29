from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login




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

def session(request):
    return render(request, 'healthcheck/session.html')  

def dashboard(request):
    return render(request, 'healthcheck/dashboard.html')

def forgotten_password(request):
    return render(request, 'healthcheck/forgotten_password.html')

def forgotten_password_confirmation(request):
    return render(request, 'healthcheck/forgotten_password_confirmation.html')

def navbar(request):
      return render(request, 'healthcheck/navbar.html')

def signup(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            
            role = form.cleaned_data['role']
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('healthcheck_home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'healthcheck/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:






    return render(request, "healthcheck/login.html")
    
    


   



