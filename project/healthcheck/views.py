from django.shortcuts import render





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

def login(request):
    return render(request, "healthcheck/login.html")

def signup(request):
      return render(request, 'healthcheck/signup.html')




def navbar(request):
      return render(request, 'healthcheck/navbar.html')


def welcome_page(request): #Nadia's task
    return render(request, 'healthcheck/welcome.html')

from django.shortcuts import render

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
