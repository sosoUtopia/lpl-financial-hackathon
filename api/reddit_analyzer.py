# praw
import praw
from praw.models.reddit.submission import Submission
from praw.models.reddit.comment import Comment

# text blob
from textblob import TextBlob

# pandas
import pandas as pd

# python
from collections import defaultdict
import configparser

# collection of stock symbols
STOCK_SYMBOLS_CSV = "./static/stocks.csv"

symbols = None
symbols = set(pd.read_csv(STOCK_SYMBOLS_CSV)["Symbol"])

config = configparser.ConfigParser()
config.read('api/config.ini')

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
    self.__comments = []
  
  def analyze(self, subreddit: str, limit=1):
    submission: Submission  
    comment: Comment
    for submission in self.__reddit.subreddit(subreddit).hot(limit=limit):
      for comment in submission.comments:
        try:
          for word in comment.body.replace("*", '').replace("$", '').split():
            if word in symbols:
              polarity = TextBlob(comment.body).polarity
              self.__sentiments[word] += polarity
              self.__comments.append({
                'comment': comment.body, 
                'symbol': word,
                'sentiment': polarity
              })
              break
        except AttributeError as e:
            pass
  
  @property
  def sentiments(self):
    return self.__sentiments

  @property
  def comments(self):
    return self.__comments
