from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class StockSentiment(models.Model):
    id = models.AutoField(primary_key=True)
    stock_symbol = models.CharField(max_length=200)
    sentiment = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    session_id = models.CharField(max_length=200)

class StockName(models.Model):
    stock_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)