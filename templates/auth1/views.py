from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
def login (request):
    if request.method=='POST':
        af=AuthenticationForm(request,data=request.POST)
        if af.is_valid():
            uname=af.cleaned_data['username']
            upass=af.cleaned_data['password']
            is_authenticate=authenticate(username=uname,password=upass)
            if is_authenticate:
                return redirect ('/app1/home/')
    else :
        f=AuthenticationForm
        content={'form':f}
        return render(request,'registration/login.html',content)