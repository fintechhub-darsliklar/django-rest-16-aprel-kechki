
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register(r"category", CategoryViewSet, basename="category")
r.register(r"product", ProductViewSet, basename="product")


urlpatterns = [
    path('', include(r.urls)),
]
