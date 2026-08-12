from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    reply = get_response(message)

    conn = sqlite3.connect("database/chat.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat(message,response) VALUES(?,?)",
        (message, reply)
    )

    conn.commit()

    conn.close()

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True, port=5007)