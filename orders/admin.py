from django.contrib import admin

from .models import Order, UserOrderDetail

admin.site.register(UserOrderDetail)
admin.site.register(Order)
# Register your models here.
