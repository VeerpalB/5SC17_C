from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.db.models import Count
from django.contrib import messages
from .models import UserProfile

from django.shortcuts import render, redirect
from .models import Vote
from django.contrib import messages
from django.utils import timezone

def department_overview(request):
    trend_labels = ["Red", "Yellow", "Green"]
    state_labels = ["worse", "stable", "improving"]

    trend_totals = [Vote.objects.filter(trend=t).count() for t in trend_labels]
    state_totals = [Vote.objects.filter(state=s).count() for s in state_labels]

    context = {
        'trend_labels': trend_labels,
        'trend_totals': trend_totals,
        'state_labels': state_labels,
        'state_totals': state_totals,
    }
    return render(request, 'healthcheck/department_overview.html', context)

def team_overview(request):
    team = request.GET.get('team')
    category = request.GET.get('category')

    votes = Vote.objects.all()

    if team:
        votes = votes.filter(team=team)  
    if category:
        votes = votes.filter(category=category)

    trend_labels = ["Red", "Yellow", "Green"]
    state_labels = ["Getting Worse", "Stable", "Improving"]

    trend_totals = [votes.filter(trend=t).count() for t in trend_labels]
    state_totals = [votes.filter(state=s).count() for s in state_labels]

    context = {
        'trend_labels': trend_labels,
        'trend_totals': trend_totals,
        'state_labels': state_labels,
        'state_totals': state_totals,
    }
    return render(request, 'healthcheck/team_overview.html', context)


def progress_view(request):
    if request.method == 'POST':
        categories = request.POST.getlist('category[]')
        trends = request.POST.getlist('trend[]')
        states = request.POST.getlist('state[]')
        notes = request.POST.getlist('note[]')
        user = request.user

        for i in range(len(categories)):
            Vote.objects.create(
                user=user,
                team=user.userprofile.team,  
                category=categories[i],
                trend=trends[i],
                state=states[i],
                note=notes[i],
                submitted_at=timezone.now()
            )

        messages.success(request, "Your votes were submitted successfully!")

    return render(request, 'healthcheck/progress.html')



def home(request):
    return render(request, 'healthcheck/home.html')

def profile(request):           
    return render(request, 'healthcheck/profile.html')

def help(request):
    return render(request, 'healthcheck/help.html')

def logout_view(request):
    return render(request, 'healthcheck/logout.html')

def voting(request):
    return render(request, 'healthcheck/voting.html')


def edit(request):
    return render(request, 'healthcheck/edit.html')


def session(request):
    return render(request, 'healthcheck/session.html')  

def dashboard(request):
    return render(request, 'healthcheck/dashboard.html')

def overview_home(request):
    return render(request, 'healthcheck/overviewhome.html')

def forgotten_password(request): # Done by Veerpal
    if request.method == 'POST':
        email = request.POST.get('email')
        messages.success(request, f"An email has been sent to {email} with password reset instructions.")
        return redirect('forgotten_password_confirmation')

    return render(request, 'healthcheck/forgotten_password.html')

def forgotten_password_confirmation(request): # Done by Veerpal
    return render(request, 'healthcheck/forgotten_password_confirmation.html')

def navbar(request):
    return render(request, 'healthcheck/navbar.html')

def signup(request):  # Done by Veerpal
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            


            role = request.POST.get('role')
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            if created:
                user_profile.role = role
                user_profile.save()
            # user_profile = UserProfile.objects.create(user=user, role=role)
            # UserProfile.objects.create(user=user, role=role)
            # user.userprofile.role = form.cleaned_data['role']
            # UserProfile.objects.create(user=user, role=role)
            # user.userprofile.role = role
            # user.userprofile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
        


        else:
            messages.error(request, "There was an error with your form. Please try again.")
            # user_profile = UserProfile.objects.create(
            #     user=user,
            #     role=form.cleaned_data['role']
            # )
            # user.email = form.cleaned_data['email']
            # user.first_name = form.cleaned_data['first_name']
            # user.last_name = form.cleaned_data['last_name']
            # user.save()
            

            
            # Save role to user profile
            # role = form.cleaned_data['role']
            
            # user_profile, created = UserProfile.objects.get_or_create(user=user)
            # user_profile.role = role
            # user_profile.save()

            # username = form.cleaned_data.get('username')
            
            


    else:
        form = CustomUserCreationForm()

    
    return render(request, 'healthcheck/signup.html', {'form': form})


def login(request): # Done by Veerpal
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # messages.success(request, f'Welcome back, {username}!')

            # Retrieve user's role
            try:
                role = user.userprofile.role
            except UserProfile.DoesNotExist:
                role = None  # or handle default


            # Role-based redirection

            if role == 'engineer':
                return redirect('home')
            
            elif role == 'teamleader':
                return redirect('home')

            elif role == 'department_leader':
                return redirect('overview_home')

            elif role == 'seniormanager':
                return redirect('welcome')

            elif role == 'admin':
                return redirect('dashboard')

            else:
                return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, "healthcheck/login.html")
    

def welcome_page(request): #Nadia's task
    return render(request, 'healthcheck/welcome.html')



def dept_overview(request): #Nadia Islam
    department = request.GET.get('department', 'Sky Design')
    date = request.GET.get('date', '2024-12-01')

    
    color_votes = [5, 10, 15]     # Red, Yellow, Green votes
    trend_votes = [4, 9, 14]      # Getting worse, Stable, Improving

    context = {
        'department': department,
        'date': date,
        'color_votes': color_votes,
        'trend_votes': trend_votes,
    }
    return render(request, 'healthcheck/dept_overview.html', context)

def senior_team_overview(request): #Nadia Islam
    team = request.GET.get('team', 'T1')
    date = request.GET.get('date', '2024-12-01')

    
    color_votes = [5, 10, 15]  # Red, Yellow, Green
    trend_votes = [4, 9, 14]   # Getting worse, Stable, Improving

    context = {
        'team': team,
        'date': date,
        'color_votes': color_votes,
        'trend_votes': trend_votes,
    }

    return render(request, 'healthcheck/senior_team_overview.html', context)