from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
	return HttpResponse("Welocme")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ok")
    else:
        form = UserCreationForm()
        return render(request)



