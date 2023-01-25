from rest_framework import serializers
from base.models import StockSentiment

class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockSentiment
        fields = '__all__'

# class StockNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         field = '__all__'
