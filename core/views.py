from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import StockSentiment
from .serializers import StockSerializer

# Create your views here.

# OLD VIEWS
# def makeStockModel(stocks : defaultdict, date, time, session : str):
#     for name, sentiment in stocks.items():
#         StockSentiment.objects.create(stock_symbol=name, sentiment=sentiment, date=date, time=time, session_id=session)

# def analyzeStockData():
#     analyzer = RedditAnalyzer()
#     analyzer.analyze('wallstreetbets', limit=1)
#     stocks = analyzer.sentiments
#     date = dt.datetime.now().date()
#     time = dt.datetime.now().time().replace(microsecond=0)
#     session = " ".join((str(date), str(time)))
#     for name, sentiment in stocks.items():
#         StockSentiment.objects.create(source="reddit", stock_symbol=name, sentiment=sentiment, date=date, time=time, session_id=session)

# @api_view(['GET'])
# def getData(request):
#     analyzeStockData()
#     stock_items = StockSentiment.objects.all()
#     serializer = StockSerializer(stock_items, many=True)
#     return Response(serializer.data)

# lists all the stocks that we analyzed from reddit and twitter or add new ones
class StockList(APIView):
    @api_view(['GET'])
    def getAllStocks(self, request=None):
        stock_items = StockSentiment.objects.all()
        serializer = StockSerializer(stock_items, many=True)
        return Response(serializer.data)

    # show and list all the stocks with the specific symbol/ticker
    @api_view(['GET'])
    def getStocksWithSymbol(self, request, symbol):
        stock_items = StockSentiment.objects.get(id=symbol)
        serializer = StockSerializer(stock_items, many=False)
        return Response(serializer.data)
    
    # show all stocks relating the session id
    # aka the date and time that they were analyzed/inserted into the database
    @api_view(['GET'])
    def getAllStocksWithSessionId(self, request, session_id):
        pass

# select/deselect stocks we want to push to alpaca to sell
class AlpacaStockOrder(APIView):
    # list all stocks that we have selected to possibly sell
    @api_view(['GET'])
    def getAllStocks(self, request=None):
        pass

    # delete all the stocks queued to the alpaca market
    @api_view(['DELETE'])
    def deleteAllStocks(self, request=None):
        pass

    # add a stock to alpaca 
    @api_view(['POST'])
    def addStock(self, request, id):
        pass