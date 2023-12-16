# BitEther_Forecast


This web application predicts stock prices based on historical data using machine learning models. Users can input stock parameters, and the application provides a predicted closing price.

## Demo

![BiEther_demo](https://github.com/Gokulachalam/BitEther_Forecast/assets/89055461/0ba4c23d-9b4d-4d40-b3a1-b4aea4484941)



## Development Environment

This project is developed and tested on a Debian 12 Linux platform



## Directory Structure

|-- app.py
|-- requirements.txt


|-- templates/
|   |-- index.html


|-- static/
|   |-- style.css


|-- data/
|   |-- ETH-BTC-USD.csv


|-- models/
|   |-- trained_model.pkl


|-- README.md
|-- .gitignore
|-- netlify.toml







## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Machine Learning Model](#machine-learning-model)
- [Contributing](#contributing)
- [License](#license)


## Features

- Predict stock prices based on historical data.
- User-friendly web interface for input and prediction.
- Clear visualization of prediction results.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Machine Learning Libraries:** scikit-learn, NumPy, pandas
- **Deployment:** Netlify (frontend), Heroku (backend)

## Getting Started

Follow these steps to get the project running on your local machine.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/stock-price-prediction.git



2. **Navigate to the project directory:**

   ```bash
   cd  BiEther_Forecast

3. **Install dependencies:**

   pip install -r requirements.txt


4. **Run the Flask app:**

   python app.py

The app will be accessible at http://localhost:5000.

**Usage**
Open the application in your web browser.
Enter stock parameters (Open, High, Low, Volume) in the provided form.
Click the "Predict" button to get the predicted closing price.
View the prediction result on the web page.


**Machine Learning Model**
The application uses an ensemble of machine learning models, including:

1.Random Forest Regressor


2.Gradient Boosting Regressor


3.AdaBoost Regressor

These models are trained on historical stock data to predict future closing prices.


## CSV Records


![Screenshot from 2023-12-11 14-00-27](https://github.com/Gokulachalam/BitEther_Forecast/assets/89055461/ae5b9316-c77d-444c-9b5e-a416168c9054)






## Parameter Inputs

![Screenshot from 2023-12-11 13-59-19](https://github.com/Gokulachalam/BitEther_Forecast/assets/89055461/c96a7a5e-d1b0-4661-8cb7-e67dd10cd0da)




## Prediction

![Screenshot from 2023-12-11 13-59-19](https://github.com/Gokulachalam/BitEther_Forecast/assets/89055461/ab58eb59-7d02-4c82-9b7c-429056c1698a)



Contributing
Feel free to contribute to the project. If you find any issues or have suggestions for improvement, please open an issue or create a pull request.


