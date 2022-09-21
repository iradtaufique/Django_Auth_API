from django.db import models
from authapp.models import User


class UserOrders(models.Model):
    orderName = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderName
