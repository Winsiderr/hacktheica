from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = [
        ('c', 'Покупатель'),
        ('s', 'Продавец'),
    ]

    userrole = models.CharField(max_length=70, choices=role, default="")
    place = models.CharField(max_length=150)