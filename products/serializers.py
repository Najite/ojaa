from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from django.contrib.auth import get_user_model
from . import models
import uuid
from users.serializers import UserSerializer

User = get_user_model


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'slug', 'link']
        read_only_fields = ['slug']
    
    def get_link(self, obj):
        request = self.context['request']
        return {
            'link': reverse('category-detail',
                            kwargs={'pk':obj.id},
                            request=request)
        }

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'slug']
        read_only_fields = ['id', 'slug']
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.CharField(source='user', read_only=True)
    # image_url = serializers.ImageField(source='image')
    category = CategorySerializer(read_only=True)
    # link = NestedHyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-detail',
    #     parent_lookup_kwargs={'product_pk': 'product_pk'}
    # )
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    url = serializers.SerializerMethodField('get_link')
    class Meta:
        model = models.Product
        fields = ['id', 'seller','name',
                   'price', 'stock',
                  'available', 'url', 'category' ] 
        read_only_fields = ['user_id', 'id'] 
        extra_kwargs = {
            'price': {'min_value': 0},
            'stock': {'min_value': 0},           
        }
        
    def get_link(self, obj):
        request = self.context['request']
        return {
            'link': reverse ('product-detail',
            kwargs={'pk':obj.id},
            request=request)
            ,            
        } 

            
        
    
         