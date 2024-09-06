from django.shortcuts import render
from .forms import AuthUserForm
# Create your views here.

def login(request):
    if(request.method == 'POST'):
        userloginform=AuthUserForm(request.POST)
        if userloginform.is_valid():
            userloginform.save()
    else:
        userloginform=AuthUserForm()
    return render(request,'users_auth/login.html',{'form':userloginform})