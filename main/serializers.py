from rest_framework import serializers
from .models import User, Product, ProductPrice

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'store_type', 'address', 'phone', 'email']

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name_nl', 'name_fr', 'mk_mc_ref', 'exp_mc_ref', 
            'mk_gy_ref', 'exp_gy_ref', 'exp_sell_price', 'mk_sell_price'
        ]

# ProductPrice serializer
class ProductPriceSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductPrice
        fields = ['id', 'product', 'price', 'creation_time']
