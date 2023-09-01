from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from products.models import Product
from .models import Cart
from .serializer import CartSerializer, CartItemSerializer

# Create your views here.
class CartList(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()  
    serializer_class = CartSerializer 
    
    # rendering a view based on the action
    
#     def get_queryset(self):
#             return Cart.objects.filter(id=self.kwargs['pk'])

class CartItem(ReadOnlyModelViewSet):
        serializer_class = CartItemSerializer
        
        def get_queryset(self):
              return Cart.objects.filter(id=self.kwargs['cart_pk'])
    
     
        
        
        
    
        
        
 
        