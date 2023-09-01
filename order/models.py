from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver 
from django.contrib.auth import get_user_model
import uuid
from products.models import Product


# custom user
User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def get_total(self):
        total = sum(item.calculate_price() for item in self.items.all())
        print(total, 'total')
        return total
    
    
    def __str__(self):
        return f'{self.user} just made an order on {self.date}'
    
     

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta: 
        unique_together = ('order', 'product', )
    
    @property
    def calculate_price(self):
        return self.quantity * self.unit_price
    
    def __str__(self):
        return f"{self.product} X {self.quantity}" 
    
        

        