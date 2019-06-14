from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, UserOrderDetail
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

# @login_required
def create(request):
    order = Order()
    order.take_spot = request.POST['order_take_spot']
    order.restaurant = request.POST['order_restaurant']
    order.balance = ""
    order.order_time = request.POST['order_time']
    order.save()
    return redirect("")

def read(request):
    read_order = Order.objects.all()
    time_now = timezone.datetime.now()
    return render(request, "orders/read.html", { 'read_order': read_order })

def new_host(request):
    return render(request, "orders/new_host.html")

def detail(request):
    return render(request, "orders/detail.html")

def new_participant(request):
    return render(request, "orders/new_participant.html")