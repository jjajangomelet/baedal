from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
from django.db import models
from django.conf import settings
from accounts.models import accounts

# Create your models here.
class Matching(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    host = models.ForeignKey(accounts, on_delete=models.CASCADE)
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
    matchingParticipant

class Brand(models.Model):
    name = models.CharField(max_length=30)
    # logo = imageField()
    


    

