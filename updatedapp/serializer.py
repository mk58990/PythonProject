from rest_framework import serializers
from .models import Foodsales

class FoodsalesSr(serializers.ModelSerializer):
    class Meta:
        model=Foodsales
        fields='__all__'