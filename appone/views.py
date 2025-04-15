from django.shortcuts import render

testdata = [
   {'id':1, 'name': 'Item 1 of list'},
   {'id':2, 'name': 'Item 2 of list'},
   {'id':3, 'name': 'Item 3 of list'},
   {'id':4, 'name': 'Item 4 of list'},
   {'id':5, 'name': 'Item 5 of list'},
   {'id':6, 'name': 'Item 6 of list'},


]


def home(request):
    return render(request, 'appone/home.html',{'testdata':testdata})