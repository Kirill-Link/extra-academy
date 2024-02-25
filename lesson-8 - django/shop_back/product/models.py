from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    quantity = models.IntegerField(verbose_name='Количество')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
