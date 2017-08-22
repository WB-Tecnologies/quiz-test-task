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
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from . import models


def index(request, Quize):
    return HttpResponse(Quize)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        success_url = "/"

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

def add_question(request):
    if request.method == "POST":
        question  = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        option5 = request.POST.get("option5")
        answer = request.POST.get("answer")
        quiz = request.POST.get("quiz")
        q = Question()
        q.question = question
        q.option1 = option1
        q.option2 = option2
        q.option3 = option3
        q.option4 = option4
        q.option5 = option5
        q.answer = answer
        q.quiz = Quiz.objects.get(pk=int(quiz))
        q.save()
        return HttpResponse("success")


