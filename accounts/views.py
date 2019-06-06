from django.shortcuts import render, redirect

from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required




# Create your views here.
# @require_http_methods(['GET', 'POST'])
def signup(request):

    return render(request, 'accounts/form.html')


# @require_http_methods(['GET', 'POST'])
def login(request):
    
    return render(request, 'accounts/form.html')


# @login_required
# @require_http_methods(['POST'])
def logout(request):
    
    return redirect('')
