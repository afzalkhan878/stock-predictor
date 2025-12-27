import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import joblib

from .feature_engineering import create_sequences

def train_lstm(df):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[['Close']])

    SEQ_LEN = 60
    X, y = create_sequences(scaled, SEQ_LEN)

    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=(SEQ_LEN,1)))
    model.add(Dropout(0.2))
    model.add(LSTM(64))
    model.add(Dense(1))

    model.compile(loss='mse', optimizer='adam')
    model.fit(X, y, epochs=10, batch_size=32, verbose=1)

    model.save("models/lstm_model.h5")
    joblib.dump(scaler, "models/scaler.pkl")

    return "Model Trained"
