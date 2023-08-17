from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import (
    Product, Category
)
from products.serializers import (
    CategorySerializer, ProductSerializer
)
# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        items = Product.objects.all()
        serialized_item = ProductSerializer(items, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_item = ProductSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED) 

        
    

@api_view(['POST'])
def product_create(request):
    serialized_item = ProductSerializer(data=request.data)
    serialized_item.is_valid(raise_exception=True) 
    serialized_item.save()
    return Response(serialized_item.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'POST'])
def product_detail(request, id):
    if request.method == 'GET':
        item = get_object_or_404(Product, pk=id)
        serialized_item = ProductSerializer(item, many=True)
        return Response (serialized_item.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        message = "Product added successfully"
        item = get_object_or_404(Product, pk=id)
        serialized_item = ProductSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response({message}, serialized_item.data, status.HTTP_201_CREATED)
    