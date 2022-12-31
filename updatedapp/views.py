from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Foodsales
from .serializer import FoodsalesSr
#Create your views here.

class FoodShow(APIView):
    def get(self,r):
        fooddetails = Foodsales.objects.all()
        serobj = FoodsalesSr(fooddetails, many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj=FoodsalesSr(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class FoodFilter(APIView):
    def get(self,r,Product):
        fooddetails=Foodsales.objects.filter(Product__iexact=Product)
        serobj=FoodsalesSr(fooddetails,many=True)
        return Response(serobj.data)

    def post(self,r,Product):
        fooddetails=Foodsales.objects.filter(Product__iexact=Product)[0:5]
        serobj=FoodsalesSr(fooddetails,many=True)
        return Response(serobj.data)

class FoodUpdateDelete(APIView):
    def put(self,r,pk):
        foodobj=Foodsales.objects.get(pk=pk)
        serobj=FoodsalesSr(foodobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        foodobj=Foodsales.objects.get(pk=pk)
        foodobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


