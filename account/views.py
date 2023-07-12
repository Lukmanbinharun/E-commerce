from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signin(request):
    if  not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            
            try:
                myuser = User.objects.create_user(email,email,password, first_name = first_name, last_name = last_name) 
                return redirect('login')
            except:
                messages.error(request,"Email already exit")
        return render(request,'signin.html')
    return redirect('home')
            
    
            
            
    

def userlogin(request):
    if  not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            # email = request.POST['email'].split('@')[0]
            password = request.POST['password']
            user = authenticate(username = email, password = password)
            if user is not None:
                login(request=request, user=user)
                return redirect('home')
            else:
                messages.info(request,'Email or Password is incorrect')
        return render(request,'login.html')
    return redirect('home')
    


def userlogout(request):
    logout(request=request)
    return redirect('login')


