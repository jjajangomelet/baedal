from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accounts(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, null=False)
    GENDER = [(0, '남'), (1, '여'),]
    gender = models.IntegerField(choices=GENDER, default=0)
    phoneNum = models.CharField(max_length=15, blank=True)
    birth_day = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100)