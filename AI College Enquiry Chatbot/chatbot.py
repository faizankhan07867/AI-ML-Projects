import json
import pickle
import random

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("model/chatbot_model.keras")

tokenizer = pickle.load(
open("model/tokenizer.pkl","rb"))

encoder = pickle.load(
open("model/label_encoder.pkl","rb"))

with open("intents.json") as file:
    intents = json.load(file)


def get_response(message):

    seq = tokenizer.texts_to_sequences(
        [message.lower()]
    )

    padded = pad_sequences(
        seq,
        maxlen=20
    )

    prediction = model.predict(
        padded,
        verbose=0
    )

    tag = encoder.inverse_transform(
        [prediction.argmax()]
    )[0]

    for intent in intents["intents"]:

        if intent["tag"] == tag:

            return random.choice(
                intent["responses"]
            )

    return "Sorry, I don't understand."