from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    currency = models.CharField(max_length=5)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=250)
    image = models.URLField()