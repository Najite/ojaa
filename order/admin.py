from django.contrib import admin
from .models import OrderItem, Order
from products.models import Product
# Register your models here.


class TabularOrder(admin.TabularInline):
    model = OrderItem  
    
    
@admin.register(Order)
class OrderItemAdmin(admin.ModelAdmin):
    inlines = [TabularOrder]
    fields = ['user', 'status', 'total', 'date']  
    
