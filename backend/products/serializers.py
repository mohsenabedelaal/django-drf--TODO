from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # this to rename the get_discount to my_discount 
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    def get_my_discount(self,obj):
        # this obj is the instance of the object passed to it
        return obj.get_discount()
