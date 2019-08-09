from django.db import models
from django.conf import settings
from accounts.models import Accounts

# Create your models here.
from django.db import models
from django.conf import settings
from accounts.models import Accounts

# Create your models here.
class Matching(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    host = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    expected_ordertime = models.DateTimeField()
    take_spot = models.CharField(max_length=255)
    banlance = models.IntegerField()
    max_user = models.IntegerField()
    

    STATUS = (
        ('P', 'PROCEEDING'),
        ('C', 'CONFIRM'),
        ('F', 'FINESHED'),
    )
    status = models.CharField(max_length = 1 , default = 'P', choices = STATUS)
    
    
 
class MatchingParticipant(models.Model):
    participant = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE)
    totalPrice = models.IntegerField()

class OrderList(models.Model):
    matchingParticipant = models.ForeignKey('MatchingParticipant', on_delete=models.CASCADE)
    name = models.CharField(max_length = 10)
    price = models.IntegerField()
    amount = models.IntegerField()

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    min_price = models.IntegerField()
    category = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
    brandImage = models.ImageField(upload_to = 'media/restaurant')
    delivery_fee = models.IntegerField(null=True, blank=True)
    # logo = imageField()


class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    foodImage = models.ImageField(upload_to = 'media/menu')
    


    

