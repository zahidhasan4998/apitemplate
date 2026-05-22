from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.product_view, name='product'),
    path('<int:id>/', views.single_product_view, name='single_product'),
    path('categories/', views.category_view, name='categories_list'),
    path('categories/<int:id>/', views.single_category_view, name='single_category')
]
