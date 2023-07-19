from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Login')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        cpassword=request.POST['password2']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email address already Exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,email=email,password=password)

                user.save();
                print('Registration Successfull')
                return redirect('login')
        else:
            messages.info(request,'Password not Matching')
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
