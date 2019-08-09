from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Matching, MatchingParticipant, OrderList, Restaurant, Menu
from datetime import datetime
from django.utils import timezone

# Create your views here.
def cover(request):
    return render(request, "orders/cover.html")

def index(request):
    return render(request, "orders/index.html")

    #create_order.balance = request.POST['create_order_balance']
    #create_order.order_time = timezone.datetime.now()

# @login_required
def create_order(request):
    create_order = Matching()
    create_order.restaurant = request.POST['create_order_restaurant']
    create_order.take_place = request.POST['create_order_take_place']
    create_order.max_user = request.POST['create_order_max_user']
    create_order.min_price = request.POST['create_order_min_price']
    create_order.balance = request.POST['create_order_balance']
    create_order.save()
    return redirect("orders:read")

def matching_list(request):
    matchings = Matching.objects.all()
   
    return render(request, "orders/matching_list.html", {'matchings' :matchings})

def new_host(request):
    return render(request, "orders/new_host.html")

def matching_detail(request, matching_id):
    matching_detail = get_object_or_404(Matching, pk = matching_id)
    return render(request, "orders/matching_detail.html", {'matching_detail' :matching_detail})

def new_participant(request):
    return render(request, "orders/new_participant.html")

def matching_create(request):
    restaurants = Restaurant.get_object_or_404
    return render(request, "orders/matching_create.html")