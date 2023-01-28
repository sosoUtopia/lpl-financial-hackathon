from rest_framework import serializers
from .models import StockSentiment

class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockSentiment
        fields = '__all__'
