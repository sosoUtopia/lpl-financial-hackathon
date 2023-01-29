from .models import StockSentiment, StockComment
from .reddit_analyzer import RedditAnalyzer
import datetime as dt

def update_stock_data(subreddit: str, limit=1):
    analyzer = RedditAnalyzer()
    analyzer.analyze(subreddit, limit)
    stocks = analyzer.sentiments
    date = dt.datetime.now().date()
    time = dt.datetime.now().time().replace(microsecond=0)
    session = " ".join((str(date), str(time)))
    for symbol, sentiment in stocks.items():
        StockSentiment.objects.create(
            source=subreddit, 
            stock_symbol=symbol, 
            sentiment=sentiment,
            date=date, time=time,
            session_id=session
        )

def update_comment_data(subreddit: str, limit=1):
    analyzer = RedditAnalyzer()
    analyzer.analyze(subreddit, limit)
    for stock in analyzer.comments:
        StockComment.objects.create(
            source=subreddit,
            symbol=stock['symbol'],
            comment=stock['comment'],
            sentiment=stock['sentiment']
        )