from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from.serializers import (
    ProductSerializer, CategorySerializer,
    CategoryDetailSerializer
    )

from .models import Product, Category

#list and create Categories
class CategoryList(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return super().get_serializer_class()
    
    # def list(self, request, category_pk=None):
    #     qs = self.queryset.filter(id=category_pk)
    #     return qs 
        
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            slug = title 
        serializer.save(slug=slug)
        
    

# List of all products
class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = serializer.data
            response['message'] = 'Product created successfully'
            return Response({
                'message': 'Product created Successfully',
                'data': response,
                }, 
                headers=headers, status=status.HTTP_201_CREATED
            )
        else:
            headers = self.get_success_headers(data=request.data)
            response = serializer.data
            response['message'] = 'Product creation failed'
            return Response({
                'message': 'Product creation failed',
                'error': response
                },
                headers=headers, status=status.HTTP_400_BAD_REQUEST,
                *args, **kwargs
            )
    
    
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        
        serializer.save(user=self.request.user,
                               )