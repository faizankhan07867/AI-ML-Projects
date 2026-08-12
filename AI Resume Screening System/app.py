from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from ats import calculate_score

app = Flask(__name__)

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Upload Resume
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file selected."

    file = request.files["resume"]

    if file.filename == "":
        return "Please choose a PDF file."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    try:
        text = extract_text(filepath)
    except Exception as e:
        return f"Resume parsing error: {e}"

    try:
        score, skills = calculate_score(text)
    except Exception as e:
        return f"ATS calculation error: {e}"

    return render_template(
        "result.html",
        score=score,
        skills=skills
    )


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("AI Resume Screening System Started")
    print("Project Folder :", BASE_DIR)
    print("Uploads Folder :", UPLOAD_FOLDER)
    print("Open Browser   : http://127.0.0.1:5001")
    print("=" * 60)

    app.run(host="127.0.0.1", port=5001, debug=True)