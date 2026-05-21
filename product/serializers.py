from rest_framework import serializers
from product.models import Product, Category
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','category','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='get_price_tax')
    def get_price_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    category = serializers.StringRelatedField()




    