from django.shortcuts import render 
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer 

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product

# Create your views here.
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Product Endpoints
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Category Endpoints
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Get Products by Category
class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Product.objects.filter(category_id=category_id)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

@api_view(['DELETE'])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
