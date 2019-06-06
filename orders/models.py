from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Order(models.Model):
    TAKE_AREA = [(0, "기숙사"), (1, "궁동"), (2, "죽동")]
    restaurant = models.CharField(max_length=255)
    area = models.IntegerField(choices=TAKE_AREA, default=0)
    take_place = models.CharField(max_length=255)
    min_price = models.IntegerField()
    delivery_price = models.BooleanField(default=False)
    max_user = models.IntegerField()
    balance = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
 
class UserOrderDetail(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    detail = models.TextField()
    price = models.IntegerField()
