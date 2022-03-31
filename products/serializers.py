from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        product = Product
        fields = ['id','title','description','inventory','price']
        