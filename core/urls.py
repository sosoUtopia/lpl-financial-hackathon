from django.urls import path
from . import views

urlpatterns = [
    path('all-stocks/', views.StockList.getAllStocks, name="all-stocks"),
]