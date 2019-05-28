from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER = [(0, '남'), (1, '여'),]
    student_id = models.CharField(max_length=9, unique=True)
    address = models.CharField(max_length=20)
    gender = models.IntegerField(choices=GENDER, default=0)