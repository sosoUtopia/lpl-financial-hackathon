import tweepy
import configparser
import pandas as pd
from collections import defaultdict
from textblob import TextBlob
import string
import numpy
from pprint import pprint

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
keywords = "nasdaq"
result_type = "popular"
limit = 100

# Class to analyze twitter stock sentiments from top search query
class TwitterAnalyzer:
    def __init__(self, twitter : tweepy.API = tweepy.API(auth)):
        if twitter:
            self.__twitter = twitter
        else:
            self.__twitter = tweepy.API(auth)
        
        self.__sentiments = {}
    
    def analyze(self, keywords : str = keywords, result_type : str = result_type, limit : int = limit):

        # twitter cursor object and creat a set of tags with twitter tags
        tweets = tweepy.Cursor(self.__twitter.search_tweets, q=keywords, count=limit, tweet_mode='extended', result_type=result_type).items(limit)
        tags = set(('#', '$', '@'))
        
        '''
        loop through every tweets
        create a set for visited tickers for current tweet so the ticker under the same tweet won't be analyzed twice
        temporary word variable to store every words in the body text
        '''
        for tweet in tweets:
            visited_tickers = set()
            word : string

            '''
            check every word in the body text of the tweet
            if the first character of the word is a tag prefix, 
            remove the prefix and end pronounciations to check if is a stock symbol
            '''
            for word in tweet.full_text.split():
                if word[0] in tags:
                    ticker : string
                    tag_type = word[0]
                    ticker = word.removeprefix(tag_type)
                    ticker.rstrip(string.punctuation)
                    '''
                    if the ticker is in symbols and not visited yet
                    add the ticker symbol in the set 
                    get the polarity of the text body
                    '''
                    if ticker in symbols and ticker not in visited_tickers:
                        visited_tickers.add(ticker)
                        user = tweet.user.screen_name
                        full_text = tweet.full_text
                        polarity = TextBlob(full_text).polarity
                        
                        '''
                            if the ticker is already analyzed from another tweet,
                            append the current tweet's user, text, and polarity 
                            to the list of individual text for the symbol,
                            then recalculate the average polarity for this symbol

                            If not analyzed already, create the symbol as the key,
                            and create a list of individual tweets under that symbol
                        '''

                        if self.__sentiments.get(ticker):
                            self.__sentiments[ticker]["individual"].append({
                                "user": user, 
                                "text": full_text, 
                                "value": polarity
                            })
                            average_ticker_sentiment = self.average_sentiment(ticker)
                            self.__sentiments[ticker]["average"] = average_ticker_sentiment
                        else:
                            self.__sentiments[ticker] = {
                                "average" : polarity,
                                "individual": [{
                                    "user" : user, 
                                    "text" : full_text, 
                                    "value": polarity
                                }]}
                else:
                    pass

    def is_not_duplicate_tweet(self, text, ticker):
        pass

    def average_sentiment(self, symbol) -> float:
        average : float
        index = 0
        list_of_sentiments = []
        while index < len(self.__sentiments[symbol]["individual"]):
            list_of_sentiments.append(self.__sentiments[symbol]["individual"][index]["value"])
            index += 1
        average = numpy.average(list_of_sentiments)
        return average

    def getCJ(self):
        pass

    @property
    def sentiments(self):
        return self.__sentiments

# twitter_analyzer = TwitterAnalyzer()
# twitter_analyzer.analyze(keywords, "mixed", limit)
# sentiments = twitter_analyzer.sentiments
# pprint(sentiments)