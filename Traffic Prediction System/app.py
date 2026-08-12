from flask import Flask, render_template, request
from predict import predict_traffic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    hour = int(request.form["hour"])
    day = int(request.form["day"])
    temperature = float(request.form["temperature"])
    rain = int(request.form["rain"])
    holiday = int(request.form["holiday"])

    result = predict_traffic(
        hour,
        day,
        temperature,
        rain,
        holiday
    )

    return render_template(
        "index.html",
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)