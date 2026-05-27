from rest_framework import serializers
from product.models import Product, Category, Review
from decimal import Decimal
from django.contrib.auth import get_user_model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','category','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='get_price_tax')
    def get_price_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    category = serializers.StringRelatedField()


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','description','product_count']

class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()


class ReviewSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Review
        fields = ['id','user','product', 'comment','ratings']
        read_only_fields = ['user','product']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)



    