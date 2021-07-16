from django.contrib import messages, auth
from django.contrib.auth import authenticate, login as dj_login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
# from .models import users
from .forms import *
# Create your views here.




def login(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']

            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    dj_login(request, user)
                    return render(request, 'dashboard.html', {'user': user, 'username': username})
                else:
                    return HttpResponse("Disabled Account")
            else:
                return render(request, 'base/login.html', {"msg": "Invalid Login"})
        else:
            return render(request, 'base/login.html', { "msg":"Invalid Login"})
    else:
        return render(request, 'base/login.html')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            return render(request, 'base/login.html')
        else:
            context = {'msg': form.errors}
            return render(request, 'base/register.html', context )
    else:
        context = { 'form': UserForm }
        return render(request, 'base/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
