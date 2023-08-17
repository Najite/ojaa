from django.db import models

class ProductManager(models.Manager):
    def get_queryset(self):
        product = super(ProductManager, self).get_queryset().filter(available=False)
        return product