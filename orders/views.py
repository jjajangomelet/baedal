from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, UserOrderDetail
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

    #create_order.balance = request.POST['create_order_balance']
    #create_order.order_time = timezone.datetime.now()

# @login_required
def create_order(request):
    create_order = Order()
    create_order.restaurant = request.POST['create_order_restaurant']
    create_order.take_place = request.POST['create_order_take_place']
    create_order.max_user = request.POST['create_order_max_user']
    create_order.min_price = request.POST['create_order_min_price']
    create_order.balance = request.POST['create_order_balance']
    create_order.save()
    return redirect("orders:read")

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