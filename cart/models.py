
from django.db import models
from django.contrib.auth.models import User
from store.models import Book

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
