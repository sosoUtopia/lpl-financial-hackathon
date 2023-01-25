from reddit_analyzer import RedditAnalyzer
from twitter_analyzer import TwitterAnalyzer
# from base import models
# from base.models import StockSentiment
from collections import defaultdict
import configparser

class StockAnalyzer():
    def __init__(self, reddit_object : RedditAnalyzer, twitter_API_object : TwitterAnalyzer):
        self.__reddit_obj = reddit_object
        self.__twitter_API_obj = twitter_API_object
        self.__combined_sentiments = defaultdict(lambda: 0)

    def combine_sentiments(self):
        reddit_sentiments = dict(self.__reddit_obj.sentiments)
        twitter_sentiments = dict(self.__twitter_API_obj.sentiments)

        for reddit_ticker in list(reddit_sentiments.keys()):
            if reddit_ticker in twitter_sentiments.keys():
                reddit_sentiment = reddit_sentiments.pop(reddit_ticker)
                twitter_sentiment = twitter_sentiments.pop(reddit_ticker)
                self.__combined_sentiments[reddit_ticker] = reddit_sentiment + twitter_sentiment
        
        self.__combined_sentiments.update(reddit_sentiments)
        self.__combined_sentiments.update(twitter_sentiments)

    def make_combined_models(self):
        pass

    @property
    def sentiments(self):
        return self.__combined_sentiments

reddit = RedditAnalyzer()
reddit.analyze("wallstreetbets", limit=10)
print("this is reddit")
print(dict(reddit.sentiments))

twitter = TwitterAnalyzer()
twitter.analyze("#stocks", "mixed", 100)
print("this is twitter")
print(dict(twitter.sentiments))

print("this is stock")
stock_analyzer = StockAnalyzer(reddit, twitter)
stock_analyzer.combine_sentiments()
combined_sentiments = stock_analyzer.sentiments

print(dict(combined_sentiments))




