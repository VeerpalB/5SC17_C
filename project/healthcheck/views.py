from django.shortcuts import render





def home(request):
    return render(request, 'healthcheck/home.html')

def profile(request):           
    return render(request, 'healthcheck/profile.html')

def progress(request):
    return render(request, 'healthcheck/progress.html')

def logout(request):
    return render(request, 'healthcheck/logout.html')



def navbar(request):
      return render(request, 'healthcheck/navbar.html')

