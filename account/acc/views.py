from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth




# Create your views here.

def home(request):
    return render(request,'a.html')

def profile(request):
    return HttpResponse("profile page")


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email_id']
        pwd=request.POST['pwd']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd)
        x.save()
        print("user careated sucessfully")
        return redirect('/')
        

    else:
        return render(request,'b.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        user=authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
        

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
    


    
