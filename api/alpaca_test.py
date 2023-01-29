from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from pprint import pprint
trading_client = TradingClient('PKQC3TFPFRRETRPNQ46H', '3FU0CyoxGTPhIah10CP0LWVg3ldDN8XCVvhcWPQV', paper=True)
# account = trading_client.get_account()
# pprint(account)

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

# orders that satisfy params
# orders = trading_client.get_orders(filter=request_params)
# pprint(orders)