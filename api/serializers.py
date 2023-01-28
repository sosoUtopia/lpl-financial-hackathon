from rest_framework import serializers
from base.models import StockSentiment, StockComment

class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockSentiment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockComment
        fields = '__all__'
