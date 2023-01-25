from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import StockSentiment
from .serializers import StockSerializer
from .reddit_analyzer import RedditAnalyzer
from collections import defaultdict
import datetime as dt

def makeStockModel(stocks : defaultdict, date, time, session : str):
    for name, sentiment in stocks.items():
        StockSentiment.objects.create(stock_symbol=name, sentiment=sentiment, date=date, time=time, session_id=session)

def analyzeStockData():
    analyzer = RedditAnalyzer()
    analyzer.analyze('wallstreetbets', limit=1)
    stocks = analyzer.sentiments
    date = dt.datetime.now().date()
    time = dt.datetime.now().time().replace(microsecond=0)
    session = " ".join((str(date), str(time)))
    for name, sentiment in stocks.items():
        StockSentiment.objects.create(source="reddit", stock_symbol=name, sentiment=sentiment, date=date, time=time, session_id=session)

@api_view(['GET'])
def getData(request):
    analyzeStockData()
    stock_items = StockSentiment.objects.all()
    serializer = StockSerializer(stock_items, many=True)
    return Response(serializer.data)