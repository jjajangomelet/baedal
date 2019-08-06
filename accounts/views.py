from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# @require_http_methods(['GET', 'POST'])
def login(request):
    return render(request, 'accounts/login.html')

def account_create(request):
    return render(request, 'accounts/account_create.html')

def signup(request):
    return render(request, 'accounts/signup.html')
