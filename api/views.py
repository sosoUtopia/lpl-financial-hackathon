# rest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .reddit_analyzer import RedditAnalyzer
from .twitter_analyzer import TwitterAnalyzer
from .alpaca_test import buyStock, sellStock
import datetime as dt

@api_view(['GET'])
def subreddit(request, pk):
    analyzer = RedditAnalyzer()
    analyzer.analyze(pk, limit=int(request.GET.get('limit', 1)))
    return Response(analyzer.sentiments)

@api_view(['GET'])
def subreddit_comments(request, pk):
    analyzer = RedditAnalyzer()
    analyzer.analyze(pk, limit=int(request.GET.get('limit', 1)))
    return Response(analyzer.comments)

@api_view(['GET'])
def home(request):
    return Response(['subreddit', 'comments'])

@api_view(['POST'])
def buy(request, symbol):
    quantity = request.GET.get('qty', 1)
    buyStock(symbol, quantity)
    return Response(f'bought {symbol}')

@api_view(['POST'])
def sell(request, symbol):
    quantity = request.GET.get('qty', 1)
    sellStock(symbol, quantity)
    return Response(f'sold {symbol}')

@api_view(['GET'])
def twitter_search(request, pk):
    analyzer = TwitterAnalyzer()
    analyzer.analyze()
    return Response(analyzer.sentiments)