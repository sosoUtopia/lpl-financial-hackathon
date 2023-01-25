# praw
import praw
from praw.models.reddit.submission import Submission
from praw.models.reddit.comment import Comment

# text blob
from textblob import TextBlob

# pandas
import pandas as pd

from collections import defaultdict

import configparser

# collection of stock symbols
STOCK_SYMBOLS_CSV = "https://raw.githubusercontent.com/sosoUtopia/reddit-paper-trading/main/reddit_paper_trader/static/stocks.csv"

symbols = None
symbols = set(pd.read_csv(STOCK_SYMBOLS_CSV)["Symbol"])
# with open(STOCK_SYMBOLS_CSV):
#     symbols = set(pd.read_csv(STOCK_SYMBOLS_CSV)["Symbol"])
config = configparser.ConfigParser()
config.read('api/config.ini')

# reddit = praw.Reddit(
#     client_id="BoDa6KhOg74QQc9A18Ph_g",
#     client_secret="mMAHfTsDDXYPm7Jkr3prv3KsSKIkWA",
#     user_agent="Stocker 1.0 by u/unknown",
# )

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    user_agent=config['reddit']['user_agent']
)
class RedditAnalyzer():
  """
  A class that analyzes stock
  """
  def __init__(self, reddit: praw.Reddit = reddit):
    self.__reddit = reddit
    self.__sentiments = defaultdict(lambda: 0)
  
  def analyze(self, subreddit: str, limit=1):
    submission: Submission  
    comment: Comment
    for submission in self.__reddit.subreddit(subreddit).hot(limit=limit):
      for comment in submission.comments:
        try:
          for word in comment.body.replace("*", '').replace("$", '').split():
            if word in symbols:
                self.__sentiments[word] += TextBlob(comment.body).polarity
        except AttributeError as e:
            pass

  def makeModels(self):
    pass
  
  @property
  def sentiments(self):
    return self.__sentiments

# instance of reddit