from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.stream import TradingStream
from .stock_analyzer import StockAnalyzer
from .models import StockSentiment
from pprint import pprint

# trading_client = TradingClient('PKQC3TFPFRRETRPNQ46H', '3FU0CyoxGTPhIah10CP0LWVg3ldDN8XCVvhcWPQV', paper=True)
# account = trading_client.get_account()
# pprint(account)
# market_order_data = MarketOrderRequest(
#                     symbol="SPY",
#                     qty=0.023,
#                     side=OrderSide.BUY,
#                     time_in_force=TimeInForce.DAY
#                     )

# # Market order
# market_order = trading_client.submit_order(
#                 order_data=market_order_data
#                )

# request_params = GetOrdersRequest(
#                     status=QueryOrderStatus.ALL,
#                     side=OrderSide.BUY
#                  )

# orders that satisfy params
# orders = trading_client.get_orders(filter=request_params)
# pprint(orders)

api_key = 'PKQC3TFPFRRETRPNQ46H'
api_secret = '3FU0CyoxGTPhIah10CP0LWVg3ldDN8XCVvhcWPQV'

class AlpacaConnector():
   def __init__(self, api_key=api_key, api_secret=api_secret, paper=True):
      self.__trading_stream = TradingStream(api_key, api_secret)
      self.__trading_client = TradingClient(api_key, api_secret, paper=True)
      self.__account = self.__trading_client.get_account()

   def create_order(self, ticker, quantity, side, time_in_force):
      pass

   def cancel_all_orders(self):
      pass

   async def stream_orders(self):
      pass

   def make_order(self, StockSentiment):
      pass

   @property
   def account(self):
      return self.__account
      