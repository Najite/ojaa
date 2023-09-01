from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Cart
import uuid
from products.models import Product


# the serializer handles the item in the cart
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product',  'quantity', 'unit_price', 'price', 'user'] 
        extra_kwargs = {
            'user': {'read_only': True,},
            'unit_price': {'read_only': True},
            'price': {'read_only': True}
            } 
        
    
# The serializer handles all the cart view api   
class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    link = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'user', 'link'] 
        extra_kwargs = {
            'user': {'read_only': True,}, 
            'id': {'read_only':True}
            } 
        
    def get_link(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(f"{obj.id}") 
        
        
    # modifying the instance to build a custom url based on id of instance
    def to_representation(self, instance):
        request = self.context['request']
        value = str(instance.id)
        if request and value in request.get_full_path(): 
            return {
                'id': instance.id,
                'user': instance.user.email,
                'link': request.build_absolute_uri("items")
            }
        return super().to_representation(instance) 