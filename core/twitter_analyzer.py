import tweepy
import configparser
import pandas as pd
from collections import defaultdict
from textblob import TextBlob

# read configs
config = configparser.ConfigParser()
config.read('api/config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

STOCK_SYMBOLS_CSV = "./static/stocks.csv"

symbols = None
symbols = set(pd.read_csv(STOCK_SYMBOLS_CSV)["Symbol"])

# searched_tweets = twitter.search_tweets(q="#stocks", lang="en", result_type="popular", count=1, until="2023-01-23")
keywords = "#stocks"
result_type = "mixed"
limit = 50

class TwitterAnalyzer:
    def __init__(self, twitter : tweepy.API = tweepy.API(auth)):
        if twitter:
            self.__twitter = twitter
        else:
            self.__twitter = tweepy.API(auth)
        self.__sentiments = defaultdict(lambda: 0)
    
    def analyze(self, keywords : str = keywords, result_type : str = result_type, limit : int = limit):
        tweets = tweepy.Cursor(self.__twitter.search_tweets, q=keywords, count=limit, tweet_mode='extended', result_type=result_type).items(limit)
        for tweet in tweets:
            try:
                for word in tweet.full_text.replace("#", "").replace("$", "").split():
                    if word in symbols:
                        self.__sentiments[word] += TextBlob(tweet.full_text).polarity
            except AttributeError as e:
                pass
    def makeModels(self):
        pass

    @property
    def sentiments(self):
        return self.__sentiments

twitter_analyzer = TwitterAnalyzer()
twitter_analyzer.analyze(keywords, "mixed", limit)
sentiments = twitter_analyzer.sentiments
print(dict(sentiments))