from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Order, UserOrderDetail
from .forms import OrderForm
from datetime import datetime

# Create your views here.
def index(request):
    orders = Order.objects.all('-pk')
    userOrderDetail = UserOrderDetail.objects.all('-pk')
    nowTime = datetime.now()
    ctx = {
        'orders': orders,
        'userOrderDeatils': userOrderDetail,
        'nowTime' : nowTime,
    }
    return render(request, 'orders/index.html', ctx)

@login_required
def create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.host = request.user
            order.save()
    else:
        