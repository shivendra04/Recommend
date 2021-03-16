from django.db import models
from products.models import Product
from user.models import User

# Recommendation model stores Recommendation of user
class Recommendation(models.Model):
    #Recommendation_Id=models.IntegerField()
    Product_id=models.IntegerField()
    User_id=models.IntegerField()
