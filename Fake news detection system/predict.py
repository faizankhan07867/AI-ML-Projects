import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

while True:

    text = input("Enter News : ")

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    if prediction == 1:
        print("Real News")

    else:
        print("Fake News")