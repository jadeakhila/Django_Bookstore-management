
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
