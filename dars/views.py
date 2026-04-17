from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializers, ProductSerializers
from .models import Category, Product


# get, post, put, patch, delete
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
