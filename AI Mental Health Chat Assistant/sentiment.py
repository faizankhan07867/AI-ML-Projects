import joblib

model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_sentiment(text):

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    return prediction