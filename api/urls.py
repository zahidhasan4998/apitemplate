from django.urls import path, include
from product.views import ProductViewset, CategoryViewset, ReviewViewset
from order.views import CartView,CartItemView,OrderViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewset, basename='products')
router.register('categories', CategoryViewset, basename='categories')
router.register('cart', CartView, basename='carts')
router.register('orders', OrderViewset, basename='orders')

nested_router = routers.NestedDefaultRouter(router,'products', lookup='product')
nested_router.register('reviews', ReviewViewset, basename='reviews_product')

cart_nested_router = routers.NestedDefaultRouter(router,'cart', lookup='cart')
cart_nested_router.register('items', CartItemView, basename='carts_list')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(cart_nested_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
