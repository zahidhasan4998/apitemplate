from django.urls import path, include
from product.views import ProductViewset, CategoryViewset, ReviewViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('categories', CategoryViewset)

nested_router = routers.NestedDefaultRouter(router,'products', lookup='product')
nested_router.register('reviews', ReviewViewset, basename='reviews_product')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls))
]
