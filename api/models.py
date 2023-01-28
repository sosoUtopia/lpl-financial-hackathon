from django.db import models

# Create your models here.
class StockSentiment(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    sentiment = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    session_id = models.CharField(max_length=100)

class StockComment(models.Model):
    source = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    symbol = models.CharField(max_length=50)
    sentiment = models.FloatField()
    