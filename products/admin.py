from django.contrib import admin
from . models import Product, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = ({'slug':('title',)})


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'price',
                    'category', 'available']




