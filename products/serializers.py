from rest_framework import serializers
from . import models
import uuid
from users.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'slug']
        

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source='user')
    # image_url = serializers.ImageField(source='image')
    category = CategorySerializer(read_only=True)
    user_id = serializers.IntegerField()
    category_id = serializers.IntegerField() 
    class Meta:
        model = models.Product
        fields = ['id', 'seller', 'title',
                   'price', 'stock',
                  'available', 'category', 'user_id', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 0},
            'stock': {'min_value': 0}
        }
        
    
        
            
            
