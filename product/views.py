from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from product.models import Product, Category, Review
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import PrductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import ProductPagination
from api.permissions import IsAdminOnly


# Create your views here.
class ProductViewset(ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = PrductFilter
    pagination_class = ProductPagination
    search_fields = ['name','description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOnly]

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.product_count <= 0:
            return Response({"message": "Category should not delete without product"})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
       
class ReviewViewset(ModelViewSet):
    def get_queryset(self):
        product_id = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_id).all()
    serializer_class = ReviewSerializer
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

