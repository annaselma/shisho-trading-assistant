import config
import json
from binance.client import Client
from datetime import datetime
import Price
import utils

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2023", "12 Jul, 2023")
json_string = json.dumps(candlesticks)
with open("./data/sample.json", "w") as outfile:
    outfile.write(json_string)

print(json_string)

def retrive_prices():
      portfolio = {'BTCUSD': '0', 'ETHUSD':'0'}
      tickers = client.get_ticker()
      for crypto in tickers:
            for asset in portfolio:
                  if crypto['symbol'] == asset:
                        portfolio[asset] = crypto['askPrice']
      return portfolio
            

def symbol_ticker(self):
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response)
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now()))