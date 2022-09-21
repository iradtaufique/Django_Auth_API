from rest_framework import serializers
from .models import UserOrders


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrders
        fields = ['id', 'orderName']


class UserOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrders
        fields = ['id', 'orderName']