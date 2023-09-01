from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Order Model import
from .models import Order, OrderItem

# Order serializes import
from .serializers import (
    OrderSerializer, OrderItemSerializer, 
    OrderDetailSerializer
)

# Create your views here.
class OrderList(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # sending a message on request
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = serializer.data
        response['message'] = 'success'
        return Response(response, headers=headers, status=status.HTTP_201_CREATED)    
    

    def get_serializer_class(self):
        if self.action == 'order_item':
            return OrderDetailSerializer
        
        return super().get_serializer_class()
            
    
    # displays the order item after related id of the order
    @action(detail=True, methods=['GET', 'POST'], url_path='item/(?P<order_id>[^/.]+)', url_name='order-order') 
    def order_item(self, request, pk=None, order_id=None):
        queryset = OrderItem.objects.filter(order__id=pk)
        serializer = OrderDetailSerializer(queryset, context={
            'request':request}                                       , many=True
        )
        return Response(serializer.data) 