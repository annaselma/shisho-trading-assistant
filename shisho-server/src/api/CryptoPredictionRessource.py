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
