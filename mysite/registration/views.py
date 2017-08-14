from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.db import models



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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password_n')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def add_quiz(request):
    if request.method == 'POST':
        quiz_name = request.POST.get("quiz_name")
        user = request.POST.get("user")
        quiz = Quiz()
        quiz.name = quiz_name
        quiz.user = User.objects.get(pk=user)
        quiz.save()
        return HttpResponse(quiz.id)

