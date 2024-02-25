import random
import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=5, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def generate_number(cls):
        number = ''.join(random.choices('0123456789', k=5))

        if not cls.objects.filter(number=number).exists():
            return number

        return cls.generate_number()

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Номер заказа'
        verbose_name_plural = 'Номера заказов'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
