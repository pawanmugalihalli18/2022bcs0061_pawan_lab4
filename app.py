from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

# Correct feature order (VERY IMPORTANT)
FEATURE_ORDER = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]

@app.get("/")
def home():
    return {"message": "Wine Quality Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    try:
        # Extract features in correct order
        features = [data[feature] for feature in FEATURE_ORDER]
        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)[0]

        # REQUIRED OUTPUT FORMAT (Lab 4)
        return {
            "name": "Pawan",
            "roll_no": "2022BCS0061",
            "wine_quality": float(prediction)
        }

    except Exception as e:
        return {
            "error": str(e)
        }