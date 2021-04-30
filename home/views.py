
import datetime
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'search.html')


def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html', {'time': time})

def feedback(request):
    return render(request, 'feedback.html')