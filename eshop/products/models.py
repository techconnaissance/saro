from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    is_active = models.BooleanField()


class Offer(models.Model):
    code = models.CharField(max_length=10)
    validFrom = models.DateField()
    validTo = models.DateField()
    discount = models.FloatField()
    description = models.CharField(max_length=255)
