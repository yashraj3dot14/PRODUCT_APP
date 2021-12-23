from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 50)
    weight = models.CharField(max_length= 10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
