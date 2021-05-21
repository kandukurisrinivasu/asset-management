from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth # for user authentication
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from .forms import LoginForm,SignUpForm #PasswordReset,EditProfileForm
from django.core.mail import send_mail
from .forms import UserDataForm
from .models import UserData
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm
from django.db.models import Q

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})



def edituser(request):
    msg = None
    success = False

    UserProfile1 = UserData.objects.all()

    User1 = User.objects.all()
    user_data = {}

    for data in User1:
        user_data['username'] = data.username
        user_data['email'] = data.email

    print(user_data)

    return render(request, "accounts/edituser_main.html", {"user": User1, "UserProfile": UserProfile1,"msg":msg, "success" : success})


def update(request, username):
    msg = None
    success = False
    User2 = User.objects.get(username=username)
    form =SignUpForm(instance=User2)

    return render(request, "accounts/edituser.html", {"form": form, "msg": msg, "success": success})






def logout(request):
    auth.logout(request)
    msg = 'You are successfully logout -login back <a href="/login">login</a>.'
    return render(request,'accounts/logout.html',{"msg":msg})


class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('/')

def add_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/add_user.html", {"form": form, "msg": msg, "success": success})

def displayUser(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        username=form.cleaned_data['username']
        name=form.cleaned_data['name']
        Location=form.cleaned_data['Location']
        Team_name=form.cleaned_data['Team_name']
        Group=form.cleaned_data['Group']
    context={'form':form,'username':username,'name':name,'Location':Location,'Team_name':Team_name,'Group':Group}
    return render(request,'index.html',context)