from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth


def oauth(request):
    return redirect('accounts/accounts_create.html')

def form(request):
    return render(request, 'accounts/form.html')


# Create your views here.
# @require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, '', {'error':'이미 사용중인 아이디입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, '', {'error': '비밀번호가 다릅니다.'})

# @require_http_methods(['GET', 'POST'])
def login(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('orders/index')
    #     else:
    #         return render(request, '', {'error' : '아이디 또는 비밀번호가 틀립니다'})
    # else:
    return render(request, 'accounts/login.html')


# @login_required
# @require_http_methods(['POST'])
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('')
    return render(request, '')
