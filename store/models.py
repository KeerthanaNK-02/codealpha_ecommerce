from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('watches', 'Watches'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    order_id = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=20, default="Processing")
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    address = models.TextField()
    items = models.TextField()
    total = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id