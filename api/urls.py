from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path, include 

# All views import
from order .views import OrderList
from products.views import ProductList, CategoryList
from cart.views import CartList, CartItem

router = DefaultRouter() 


router.register(r'orders', OrderList, basename='order'),

router.register(r'products', ProductList, basename='product')
router.register(r'categories', CategoryList, basename='category')

router.register(r'carts', CartList)

products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')

category_router = routers.NestedDefaultRouter(router, r'categories', lookup='category')

cart_router = routers.NestedDefaultRouter(router, r'carts', lookup='cart')
cart_router.register('items',CartItem, basename='cart-detail' )
  
urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls)),
    path("", include(category_router.urls)),
    path("", include(cart_router.urls))
]

 
 

