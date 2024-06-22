from binance.client import Client
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import pickle

app = Flask(__name__)
CORS(app)
API_KEY = ""
API_SECRET = ""
client = Client(API_KEY, API_SECRET)


@app.route('/api/v2/trading-datas/<symbol>/<interval>', methods=['GET'])
def retrieveBinanceDataBy():
    #if client.status_code != 200:
        # return jsonify({
        #     'status': 'error',
        #     'message': 'La requête à l\'API n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        # }), 500
    return jsonify({
        'status': 'ok',
        'data': "data"
    })
@app.route('/api/history')
def retrieve_history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Janv, 2023", "15 Jun, 2024")
    datas = []
    for data in candlesticks:
        timestamp = data[0] / 1000  # Convert milliseconds to seconds
        date_time = datetime.fromtimestamp(timestamp)
        candlesticks = {
            "time": date_time.strftime('%Y-%m-%d %H:%M:%S'),
            "open":data[1],
            "high":data[2],
            "low": data[3],
            "close": data[4]
        }
        datas.append(candlesticks)
        #json_file = json.loads(jsonify(datas))
        #write_csv_file(json_file)
    return jsonify(datas)

    # Load the ARIMA model
def load_arima_model():
    with open('arima_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Endpoint for making predictions
@app.route('api/predict', methods=['POST'])
def predict():
    # Get JSON input data
    data = request.get_json()

    # Example: Load time series data (assuming it's provided in the request)
    # Replace this with your actual data handling logic
    # For example, you may load data from a file path or database
    
    ##time_series_data = df.DataFrame(data['time_series'])

    # Number of steps ahead to forecast
    steps = data['steps']

    # Load ARIMA model
    model = load_arima_model()

    # Make predictions
    forecast = model.forecast(steps)[0]

    # Prepare JSON response
    response = {
        'forecast': forecast.tolist()
    }

    return jsonify(response)


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
