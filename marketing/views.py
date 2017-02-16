from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>w00t!</h1>')
    return render(request, 'core/home.html')

def history(request):

    context = {
        'dob': 'August 31, 1989',
        'full_name': 'Alex Koepke',
        'first_name': 'Alex',
    }

    return render(request, 'history.html', context)

def contact(request):

    context = {
        'phone_number': '(513) 236-7281',
        'email': 'alex.koepke@gmail.com',
    }

    return render(request, 'contact.html', context)
