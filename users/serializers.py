from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(read_only=True, source='user')
    class Meta:
        model = User
        fields = ['seller']