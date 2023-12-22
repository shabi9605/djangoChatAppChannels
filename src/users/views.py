
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
# from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("invalid username or password")
    else:
        return render(request,'user/login.html')