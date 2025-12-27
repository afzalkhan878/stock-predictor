import numpy as np
from tensorflow.keras.models import load_model
import joblib

def predict_next(df):
    model = load_model("models/lstm_model.h5")
    scaler = joblib.load("models/scaler.pkl")

    data = scaler.transform(df[['Close']])
    last_60 = data[-60:]
    last_60 = np.expand_dims(last_60, axis=0)

    pred = model.predict(last_60)
    prediction = scaler.inverse_transform(pred)[0][0]

    return prediction
