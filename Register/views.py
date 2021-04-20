from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth # for user authentication
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username,password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential!")
            return redirect("login")

    else:
        return render(request, 'login.html')



def register(request):
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name, mobile=mobile)
                user.save()
                messages.info(request, 'user created succesfully!')
                return redirect('login') ## if user is successfully created redirect login page.
        else:
            messages.info(request, 'password not matching!')
            return redirect('register')



    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')