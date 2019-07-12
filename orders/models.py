from django.db import models
from django.conf import settings
from accounts.models import User

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
    banlance = modles.IntegerField()
    max_user = models.IntegerField()
    delivery_price = models.BooleanField(default=0)

    STATUS = (
        ('P', 'PROCEEDING'),
        ('C', 'CONFIRM'),
        ('F', 'FINESHED'),
    )
    status = models.ChareField(max_length = 1 , default = 'P', choices = STATUS)
    
    
 
class MatchingParticipant(models.Model):
    participant = models.ForeignKey(accounts, on_delete=models.CASCADE)
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
    category = models.charField()
    address = models.charField()
    contact = models.charField()
    brandImage = models.ImageField(upload_to)
    # logo = imageField()
    


    

