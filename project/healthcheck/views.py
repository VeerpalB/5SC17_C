from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages





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

<<<<<<< HEAD
def signup(request):
      return render(request, 'healthcheck/signup.html')

=======
def dashboard(request):
    return render(request, 'healthcheck/dashboard.html')
>>>>>>> 514e73cac4ef398b1b035e029ece1dbde4cdb73f

def overview_home(request):
    return render(request, 'healthcheck/overview_home.html')


def department_overview(request):
    return render(request, 'healthcheck/department_overview.html')


def team_overview(request):
    return render(request, 'healthcheck/team_overview.html')

def forgotten_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        messages.success(request, f"An email has been sent to {email} with password reset instructions.")
        return redirect('forgotten_password_confirmation')

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
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('healthcheck_home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, "healthcheck/login.html")
    
    


   




def welcome_page(request): #Nadia's task
    return render(request, 'healthcheck/welcome.html')



def dept_overview(request):
    department = request.GET.get('department', 'Sky Design')
    date = request.GET.get('date', '2024-12-01')

    # Later you'll fetch real data based on department + date
    color_votes = [5, 10, 15]     # Red, Yellow, Green votes
    trend_votes = [4, 9, 14]      # Getting worse, Stable, Improving

    context = {
        'department': department,
        'date': date,
        'color_votes': color_votes,
        'trend_votes': trend_votes,
    }
    return render(request, 'healthcheck/dept_overview.html', context)

def senior_team_overview(request):
    team = request.GET.get('team', 'T1')
    date = request.GET.get('date', '2024-12-01')

    # DUMMY DATA — replace with real queries later
    color_votes = [5, 10, 15]  # Red, Yellow, Green
    trend_votes = [4, 9, 14]   # Getting worse, Stable, Improving

    context = {
        'team': team,
        'date': date,
        'color_votes': color_votes,
        'trend_votes': trend_votes,
    }

    return render(request, 'healthcheck/senior_team_overview.html', context)