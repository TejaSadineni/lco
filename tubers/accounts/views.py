from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are Logged in")
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect(login)
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
                messages.warning(request,'Username Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    user.save()
                    messages.success(request,'Account Created Successfully')
                    return redirect('login')
        else:
            messages.warning(request,'Password do not match')
            return redirect('register')

        return redirect('login')


    return render(request,'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
