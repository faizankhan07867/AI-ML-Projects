from pathlib import Path
import joblib

from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent

MODEL = BASE_DIR / "model"

model = joblib.load(MODEL / "model.pkl")
vectorizer = joblib.load(MODEL / "vectorizer.pkl")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]

    vector = vectorizer.transform([news])

    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "✅ Real News"
    else:
        result = "❌ Fake News"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)