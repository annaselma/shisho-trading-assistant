from binance.client import Client
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import configparser
import os
from flask_restx import Api, Resource, fields

app = Flask(__name__)
CORS(app)

# Initialize Flask-RESTx API
api = Api(app, version='1.0', title='Binance API',
          description='A simple Binance API to retrieve historical data',
          doc='/docs')  # Swagger UI will be available at http://127.0.0.1:5000/docs

# Define the namespace
ns = api.namespace('api', description='Binance operations')

config = configparser.ConfigParser()

# Ensure the config file exists before reading
config_file = "../config.ini"
if not os.path.exists(config_file):
    raise FileNotFoundError(f"{config_file} not found. Please ensure it exists.")

config.read(config_file)

# Ensure the 'binance' section exists
if "binance" not in config:
    raise KeyError("'binance' section not found in the config file.")

key = config["binance"].get("api_key", None)
secret = config["binance"].get("api_secret", None)

if not key or not secret:
    raise ValueError("API key and/or secret missing in the config file.")

# Define the request parser and response model for documentation
history_response = api.model('Candlestick', {
    'time': fields.String(description='The timestamp of the candlestick'),
    'open': fields.String(description='The opening price'),
    'high': fields.String(description='The highest price'),
    'low': fields.String(description='The lowest price'),
    'close': fields.String(description='The closing price')
})

@ns.route('/_queryBinanceDatas')
class QueryBinanceDatas(Resource):
    @api.doc(params={
        'symbol': {'description': 'The trading pair symbol', 'default': 'cryptoCurrency(BTCUSD..)'},
        'interval': {'description': 'The candlestick interval (e.g., 1m, 5m, 1h)', 'default': '1h'},
        'start_date': {'description': 'The start date for the historical data', 'default': '1 Jan, 2023'},
        'end_date': {'description': 'The end date for the historical data', 'default': '15 Jun, 2024'}
    })
    @api.marshal_list_with(history_response)
    def get(self):
        """
        Retrieve historical binance data from binance api.
        """
        client = Client(key, secret)
        
        # Get parameters from the request (with defaults)
        symbol = request.args.get('symbol', default='BTCUSDT')
        interval = request.args.get('interval', default=Client.KLINE_INTERVAL_1HOUR)
        start_date = request.args.get('start_date', default="1 Jan, 2023")
        end_date = request.args.get('end_date', default="15 Jun, 2024")
        
        candlesticks = client.get_historical_klines(symbol, interval, start_date, end_date)
        datas = []
        for data in candlesticks:
            timestamp = data[0] / 1000  # Convert milliseconds to seconds
            date_time = datetime.fromtimestamp(timestamp)
            candlestick = {
                "time": date_time.strftime('%Y-%m-%d %H:%M:%S'),
                "open": data[1],
                "high": data[2],
                "low": data[3],
                "close": data[4]
            }
            datas.append(candlestick)
        
        return datas

@ns.route('/history')
class History(Resource):
     @api.doc(params={
        'symbol': {'description': 'The trading pair symbol', 'default': 'cryptoCurrency(BTCUSD..)'},
        'interval': {'description': 'The candlestick interval (e.g., 1m, 5m, 1h)', 'default': '1h'},
        'start_date': {'description': 'The start date for the historical data', 'default': '1 Jan, 2023'},
        'end_date': {'description': 'The end date for the historical data', 'default': '15 Jun, 2024'}
    })
     @api.marshal_list_with(history_response)
     def retrieveHistoricalDatas(self):
        """
        Retrieve historical binance datas from database
        """
     client = Client(key, secret)

if __name__ == "__main__":
    app.run(debug=False, threaded=True, port=5000)
