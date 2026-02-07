# Task 2 - House Price Prediction using Linear Regression

## Project Description
This project builds a Linear Regression model to predict house prices based on multiple features such as rooms, size, location, and other house attributes.

The dataset is loaded from a CSV file and preprocessed using Scikit-learn pipelines.

## Folder Structure
```
Task2_House_Price_Prediction/
│── data/
│     └── house_data.csv
│── model_training.py
│── requirements.txt
│── README.md
│── output/
│     └── predictions.csv
```

## Installation
```bash
pip install -r requirements.txt
```

## Run the Project
```bash
python model_training.py
```

## Output
- Trained model saved as: `house_price_model.pkl`
- Predictions saved as: `output/predictions.csv`

## Evaluation Metrics
- MAE
- MSE
- RMSE
- R² Score

## Observations
- Missing values are handled using median (numeric) and most frequent (categorical).
- Categorical columns are encoded using OneHotEncoder.
- Linear Regression provides a baseline model for house price prediction.
