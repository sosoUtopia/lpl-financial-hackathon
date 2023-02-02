from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='reddit'),
    path('subreddit/comments/<str:pk>/', views.subreddit_comments, name='comments'),
    path('subreddit/<str:pk>/', views.subreddit, name='reddit'),
    path('subreddit/buy/<str:symbol>', views.buy, name='buy'),
    path('subreddit/sell/<str:symbol>', views.sell, name='sell'),
    path('twitter/search/<str:pk>', views.twitter_search, name="twitter search"),
]