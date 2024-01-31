import os

from binance.client import Client
from flask import Flask, render_template, jsonify
from binance.enums import *

app = Flask(__name__)
API_KEY = "PWn5MNfr50Ku9dVmcegIqkFdX4lPiM28eE7hlcjKG5GefHn6spRFSqZyby7EQa4S"
API_SECRET = "Vhi4Az5K3IZPHZud8zmO7Cgw72hCzF7APGOKXzTlu3dpAiNM0txs4D1tILxOgEGf"
client = Client(API_KEY, API_SECRET)
 
@app.route('/api/v2/trading-datas/<symbol>/<interval>', methods=['GET'])
def retrieveBinanceDataBy():
    #if client.status_code != 200:
        # return jsonify({
        #     'status': 'error',
        #     'message': 'La requête à l\'API météo n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        # }), 500
    return jsonify({
      'status': 'ok', 
      'data': "data"
    })

@app.route('/')
def index():
    title = 'BinanceView'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route('/history')
def retrieve_history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Jul, 2023", "12 Jul, 2023")
    datas = []
    for data in candlesticks:
        candlesticks = {
            "time": data[0]/1000,
            "open":data[1],
            "high":data[2],
            "low": data[3],
            "close": data[4]
        }
        datas.append(candlesticks)
    return jsonify(datas)



# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
