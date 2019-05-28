from django.shortcuts import render, redirect

from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import UserCustomCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('')
    else:
        form = UserCustomCreationForm()
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/form.html', ctx)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('')
    else:
        form = AuthenticationForm()
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/form.html', ctx)


@login_required
@require_http_methods(['POST'])
def logout(request):
    auth_logout(request)
    return redirect('')
