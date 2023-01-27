from django.contrib import admin

# Register your models here.

from .models import StockSentiment, StockOrder

admin.site.register(StockSentiment)
admin.site.register(StockOrder)
