from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from predict import predict

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- Home ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------- Show Uploaded Image -----------
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ------------- Predict ----------------
@app.route("/predict", methods=["POST"])
def prediction():

    if "image" not in request.files:
        return "No file selected"

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    disease, confidence = predict(filepath)

    return render_template(
        "index.html",
        disease=disease,
        confidence=confidence,
        image=filename
    )


# ------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)