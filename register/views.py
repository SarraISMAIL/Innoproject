from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    return render(request,'register.html')
def userregister(request):
    msg=''
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if User.objects.filter(username=username).exists():
        msg="username already exists"
        return render(request,'register.html',{'error':msg,'rep':False})
    elif password1 != password2 :
        msg="passwords miss matched"
        return render(request,'register.html',{'error':msg,'rep':False})
    else:
        user = User.objects.create_user(username,email,password2)
        user.save()
        return render(request,'register.html',{'rep':True})
