from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    price = models.FloatField()
    price_discount = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    items = models.CharField(max_length=600)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    total = models.CharField(max_length=10)
