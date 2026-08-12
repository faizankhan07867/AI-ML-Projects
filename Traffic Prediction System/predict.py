import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict_traffic(hour, day, temperature, rain, holiday):

    data = np.array([[hour, day, temperature, rain, holiday]])

    prediction = model.predict(data)

    return round(prediction[0], 2)