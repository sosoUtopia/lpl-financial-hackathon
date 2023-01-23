from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from base.models import StockSentiment
from .serializers import StockSerializer
from .serializers import ItemSerializer
from . import stock_analyzer 
from collections import defaultdict
import datetime as dt
# @api_view(['GET'])
# def getData(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     # person =  {"name" : "dennis", "age" : 28}
#     return Response(serializer.data)

@api_view(['GET'])
def getData(request):
    analyzer = stock_analyzer.StockAnalyzer(stock_analyzer.reddit)
    analyzer.analyze('wallstreetbets', limit=10)
    stocks = analyzer.sentiments
    print(stocks)
    date = dt.datetime.now().date()
    time = dt.datetime.now().time()
    session = " ".join((str(date), str(time)))
    for name, sentiment in stocks.items():
        StockSentiment.objects.create(stock_symbol=name, sentiment=sentiment, date=date, time=time, session_id=session)
    stock_items = StockSentiment.objects.all()
    serializer = StockSerializer(stock_items, many=True)
    return Response(serializer.data)