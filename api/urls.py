from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='reddit'),
    path('subreddit/comments/<str:pk>/', views.subreddit_comments, name='comments'),
    path('subreddit/<str:pk>/', views.subreddit, name='reddit'),
]