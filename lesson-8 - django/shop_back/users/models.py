from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    credit_card = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
