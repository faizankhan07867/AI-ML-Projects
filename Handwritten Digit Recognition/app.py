from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import base64
import io

app = Flask(__name__)

model = load_model("model.h5")


# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/")
def home():
    return "<h1>HANDWRITTEN DIGIT RECOGNITION PROJECT</h1>"


@app.route("/predict", methods=["POST"])
def predict():

    image = request.form["image"]

    image = image.split(",")[1]

    image = base64.b64decode(image)

    img = Image.open(io.BytesIO(image)).convert("L")

    img = img.resize((28, 28))

    img = np.array(img)

    img = 255 - img

    img = img / 255.0

    img = img.reshape(1, 28, 28)

    prediction = model.predict(img)

    digit = int(np.argmax(prediction))

    return jsonify({"digit": digit})


if __name__ == "__main__":
    app.run(debug=True, port=5050)