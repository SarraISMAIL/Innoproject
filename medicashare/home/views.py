from django.shortcuts import render ,redirect
def index(request):
    if request.user.is_authenticated :
        return redirect(f'/profile/')
    return render(request,'index.html')
