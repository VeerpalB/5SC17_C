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




def navbar(request):
      return render(request, 'healthcheck/navbar.html')

