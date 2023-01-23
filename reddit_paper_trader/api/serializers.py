from rest_framework import serializers
from base.models import Item
from base.models import StockSentiment
from base.models import StockName

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockSentiment
        fields = '__all__'

# class StockNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         field = '__all__'
