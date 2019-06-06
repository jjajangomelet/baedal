from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Order, UserOrderDetail

from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "orders/index.html")


# @login_required
def create(request):
    return redirect("")

def read(request):
    return render(request, "orders/read.html")

def new(request):
    return render(request, "orders/new.html")

def detail(request):
    return render(request, "orders/detail.html")