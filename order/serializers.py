from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import OrderItem, Order
from products.models import Product

# a serializer that handles order and order item
class OrderItemSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = ['order', 'id', 'product',
                  'quantity', 'unit_price', 'url']
        
    def get_url(self,obj):
        request = self.context['request']
        return request.build_absolute_uri(f"{obj.order.id}/item/{obj.id}")
        
        
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    items = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 
                  'date', 'items',]


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'id', 'product',
                  'quantity', 'unit_price']
        
    

        
    
    
         
    
    