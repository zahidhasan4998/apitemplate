from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer 
from product.models import Product, Category


# Create your views here.
@api_view()
def product_view(request):
    product = Product.objects.select_related('category').all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view()
def single_product_view(request, id):
    single_product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(single_product)
    return Response(serializer.data)

@api_view()
def category_view(request):
    return Response("categories")
