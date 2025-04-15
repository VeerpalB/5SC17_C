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

def blist(request,id):
      listitem = None

      for i in testdata:
           
           if i ['id'] == int(id):
                listitem = i
                
                context = {'listitem':listitem}
      return render(request, 'appone/blist.html', context)


def navbar(request):
      return render(request, 'appone/navbar.html')