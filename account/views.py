
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import *

# Create your views here.
#def home(request):
 #   return render(request,'home.html')
#@login_required
#def Dashboard(request):
#    return render(request,'Dashboard.html')

#def register(request):
#    if request.method=='POST':
 #       form=UserCreationForm(request.POST)
  #      if form.is_valid():
   #         form.save()
    #        return redirect('login_url')

    #else:
     #   form=UserCreationForm()

    #return render(request,'registration/register.html',{'form':form})

from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from .forms import editForm


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
sender='saikatkiit218@gmail.com'
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST,request.FILES)
        sub="Welcome to the EBB Tracking tool"
        Message= "You hace successfully registered in Bosch EBB tracking tools"
        recipient=str(form['email'].value())
        send_mail(sub,Message, sender,[recipient],fail_silently=False)
        html = 'we have recieved this form again'
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request,'error.html')
            user_pr.save()
            html=html+"The form is valid"
    else:
        html = 'welcome to EBB asset tracking tool for the first time'
    return render(request, 'signup.html', {'html': html, 'form': form})

def updateProfile(request):
    u_form=forms.editForm()
    if request.method=='POST':
        u_form = forms.editForm(request.POST,request.FILES,instance=request.user)
        html='We recieved update page'
        if u_form.is_valid():
            user_pr = u_form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            user_pr.save()
            html=html + 'the update form is valid'

    else:
        html='Welcome to the udate page'
        #u_form = forms.editForm(instance=request.user)

    return render(request, 'update.html', {'html':html, 'form':u_form})

def excelUpload(request):
    assets= assetOwner.objects.all()
    context={
        'Asset':assets,
        'Header':'Asset details'
    }
    return render(request, 'excel.html' ,context)




