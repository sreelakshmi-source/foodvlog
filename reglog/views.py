from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username=request.POST['username']
        email = request.POST['email']
        psw1 = request.POST['psw']
        psw2=request.POST['psw-repeat']
        if psw1 == psw2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'user already exist' )
                return redirect('login')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=psw1)
                user.save()
                return redirect('login')

        else:
           messages.info(request,'password not matching...')
           return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            print('het')
            return redirect('login')


    return render(request,'login.html')


def logout (request):
    auth.logout(request)
    return redirect('/')