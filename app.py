from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained linear regression model (theta parameters)
theta_best = joblib.load('linear_regression_model.joblib')

@app.route('/')
def home():
    return "Lightweight Linear Regression API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        X_new = np.array(data['input'])  # Expecting a 2D array of input features
        X_new_b = np.c_[np.ones((len(X_new), 1)), X_new]  # Add x0 = 1 for bias term
        predictions = X_new_b.dot(theta_best)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

