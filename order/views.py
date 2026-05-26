from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from order.models import Cart, CartItem
from order.serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer,QuantityUpdateSerializer

# Create your views here.
class CartView(GenericViewSet,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemView(ModelViewSet):
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        self.http_method_names = ['get','post','patch','delete']
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return QuantityUpdateSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
