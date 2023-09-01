from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.utils.text import slugify
from .manager import ProductManager
from .validate import validate_price
# Create your models here.

User = get_user_model()


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(null=True, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
# product model
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='media/products', null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, 
                                default=0, db_index=True, 
                                validators=[validate_price],
                                )
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=False, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    objects = ProductManager()
    
    def __str__(self):
        return self.name
    
    


        
        