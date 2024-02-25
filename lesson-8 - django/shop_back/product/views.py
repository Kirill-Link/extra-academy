from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id, is_active=True)


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True, quantity__gt=0)
    serializer_class = ProductSerializer

