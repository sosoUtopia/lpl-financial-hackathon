from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read('api/config.ini')

api_key = config["alpaca_trader"]["api_key"]
api_key_secret = config["alpaca_trader"]["api_key_secret"]

trading_client = TradingClient('PKQC3TFPFRRETRPNQ46H', '3FU0CyoxGTPhIah10CP0LWVg3ldDN8XCVvhcWPQV', paper=True)

def buyStock(stockName, quantity): 
   # preparing the orders
   # params: qty:[double] -> amt to buy
   #         notional:[double] -> $amt to by
   market_order_data = MarketOrderRequest(
                     symbol= stockName,
                     qty = quantity,
                     side=OrderSide.BUY,
                     time_in_force=TimeInForce.GTC
                     )

   # Placing market order
   market_order = trading_client.submit_order(
                  order_data=market_order_data
                  )

def sellStock(stockName, quantity): 
   # preparing the orders
   # params: qty:[double] -> amt to buy
   #         notional:[double] -> $amt to by
   market_order_data = MarketOrderRequest(
                     symbol= stockName,
                     qty = quantity,
                     side=OrderSide.SELL,
                     time_in_force=TimeInForce.GTC
                     )

   # Placing market order
   market_order = trading_client.submit_order(
                  order_data=market_order_data
                  )

                  