from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def log_in(request):
    return render(request,'login.html')
#
def userlogin(request):
    username =request.POST['username']
    password = request.POST['password']
    User = authenticate(username=username,password=password)
    if User is not None :
        login(request,User)
        return render(request,'main.html',{'user':username})
    else:
        msg="username or password invalid"
        return render(request,'login.html' ,{'msg':msg})
@login_required      
def userlogout(request):
    logout(request)
    return redirect('/')
