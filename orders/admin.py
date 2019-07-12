from django.contrib import admin

from .models import Order, UserOrderDetail, Restaurant, Brand

admin.site.register(UserOrderDetail)
admin.site.register(Order)
admin.site.register(Restaurant)
admin.site.register(Brand)
# Register your models here.
