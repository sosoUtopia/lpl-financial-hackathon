# rest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .reddit_analyzer import RedditAnalyzer
import datetime as dt

@api_view(['GET'])
def subreddit(request, pk):
    analyzer = RedditAnalyzer()
    analyzer.analyze(pk, limit=request.GET.get('limit', 1))
    return Response(analyzer.sentiments)

@api_view(['GET'])
def subreddit_comments(request, pk):
    analyzer = RedditAnalyzer()
    analyzer.analyze(pk, limit=request.GET.get('limit', 1))
    return Response(analyzer.comments)

@api_view(['GET'])
def home(request):
    return Response(['subreddit', 'comments'])