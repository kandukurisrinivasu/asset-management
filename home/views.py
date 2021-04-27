
import datetime
from django.shortcuts import render

def home(request):
    return render(request, 'home1.html')


def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html', {'time': time})

def feedback(request):
    return render(request, 'feedback.html')