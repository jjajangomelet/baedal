from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, UserOrderDetail
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

# @login_required
def create(request):
    create_order = Order.objects.all('-pk')
    create_order.take_spot = ""
    create_order.restaurant = ""
    create_order.balance = ""
    create_order.order_time = ""
    return redirect("")

def read(request, order_id):
    read_order = Order.objects.all()
    return render(request, "orders/read.html", { 'read_order': read_order})

def new(request):
    return render(request, "orders/new.html")

def detail(request):
    return render(request, "orders/detail.html")