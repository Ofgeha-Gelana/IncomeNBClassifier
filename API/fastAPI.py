from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Load trained models
with open("gaussian_nb.pkl", "rb") as f:
    gnb_model = pickle.load(f)

with open("logistic_regression.pkl", "rb") as f:
    lr_model = pickle.load(f)

# Initialize FastAPI
app = FastAPI()

# Define input data model
class IncomeData(BaseModel):
    age: int
    workclass: str
    education: str
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    native_country: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int

# Function to preprocess input data
def preprocess(data: IncomeData):
    df = pd.DataFrame([data.dict()])
    # Convert categorical variables using the same preprocessing as training
    df = pd.get_dummies(df)
    return df

# Prediction endpoint
@app.post("/predict/{model_type}")
def predict(model_type: str, data: IncomeData):
    processed_data = preprocess(data)

    if model_type == "gaussian":
        prediction = gnb_model.predict(processed_data)[0]
        prob = gnb_model.predict_proba(processed_data).max()
    elif model_type == "logistic":
        prediction = lr_model.predict(processed_data)[0]
        prob = lr_model.predict_proba(processed_data).max()
    else:
        return {"error": "Invalid model type. Use 'gaussian' or 'logistic'."}

    return {
        "model": model_type,
        "prediction": ">50K" if prediction == 1 else "<=50K",
        "probability": round(prob, 4)
    }

# Run API
# uvicorn filename:app --reload
