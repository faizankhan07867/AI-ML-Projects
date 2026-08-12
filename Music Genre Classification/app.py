from flask import Flask, render_template, request
import os
from predict import predict_genre

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["audio"]

    if file.filename == "":
        return render_template(
            "index.html",
            result="Please Select Audio File"
        )

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(path)

    genre = predict_genre(path)

    return render_template(
        "index.html",
        result=genre
    )

if __name__ == "__main__":
    app.run(debug=True)