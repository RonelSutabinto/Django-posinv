from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.


def dashboard(request):
    #if request.user.is_authenticated:
    #    return render(request, 'dashboard.html')
    #else:
    return render(request, 'base/login.html')