from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='products/', blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} : {self.price}"
    