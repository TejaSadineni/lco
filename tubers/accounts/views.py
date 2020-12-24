from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def login(request):
    return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cnfpassword = request.POST['cnfpassword']

        if password == cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    user.save()
                    messages.success(request,'Account Created Successfully')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')

        return redirect('login')


    return render(request,'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request,'accounts/dashboard.html')
