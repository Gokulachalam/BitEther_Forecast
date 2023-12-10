from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

app = Flask(__name__)

# Load the CSV file
file_path = '/home/gokul/Documents/myproject/ETH-BTC-USD.csv'
data = pd.read_csv(file_path)

# Preparing the data for the prediction model
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'
data_cleaned = data.dropna()
X = data_cleaned[features]
y = data_cleaned[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensemble Learning Models
models = {
    'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
    'GradientBoosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
    'AdaBoost': AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=100, random_state=42)
}

# Dictionary to store the RMSE for each model
rmse_scores = {}

# Train the models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    rmse_scores[name] = rmse

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        open_val = float(request.form['open'])
        high_val = float(request.form['high'])
        low_val = float(request.form['low'])
        volume_val = float(request.form['volume'])

        # Create a DataFrame with the input data
        input_data = {
            'Open': [open_val],
            'High': [high_val],
            'Low': [low_val],
            'Volume': [volume_val]
        }
        input_df = pd.DataFrame(input_data)

        # Finding the best model based on RMSE
        best_model_name = min(rmse_scores, key=rmse_scores.get)
        best_model = models[best_model_name]

        # Make predictions using the best model
        prediction = best_model.predict(input_df)

        return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
