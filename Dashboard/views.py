from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def search(request):
    return render(request, 'search.html')

def upload(request):
    if request.method=='POST':
        file=request.FILES['myFile']
        csv=pd.read_csv(file)
        print(csv.head())
        arr=csv['sum']
        sum =sum(arr)
        return render(request, 'upload.html',{"something":True, "sum":sum})
    else:
        return render(request, 'upload.html')