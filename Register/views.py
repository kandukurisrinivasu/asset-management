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

    return render(request, "accounts/edituser.html", {"user": User1, "UserProfile": UserProfile1,"msg":msg, "success" : success})


def update(request, username):
    msg = None
    success = False
    # User.objects.all()
    User2 = User.objects.get(username=username)
    # UserProfile2 = UserProfile.objects.get(user=username)
    form =SignUpForm(instance=User2)
    # profile_form = UserProfileForm(instance=UserProfile2)

    return render(request, "accounts/edituser.html", {"form": form, "msg": msg, "success": success})


def logout(request):
    auth.logout(request)
    return redirect('/')

