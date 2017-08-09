from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User


# def index(request):
    # return HttpResponse("Welocme")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/registration/loggedin/")
    else:
        return HttpResponseRedirect("/registration/invalid/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/registration/loggedout/")
