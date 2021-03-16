from django.db import models

# Create your models here.
class Product(models.Model):
    Pid=models.IntegerField()
    shape=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    location=models.CharField(max_length=256)
    price=models.FloatField()
