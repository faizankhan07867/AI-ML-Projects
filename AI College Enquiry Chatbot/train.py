import os
import json
import pickle

from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# -----------------------------
# Create model folder
# -----------------------------
os.makedirs("model", exist_ok=True)

# -----------------------------
# Load intents
# -----------------------------
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

sentences = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern.lower())
        labels.append(intent["tag"])

# -----------------------------
# Tokenizer
# -----------------------------
tokenizer = Tokenizer(
    num_words=5000,
    oov_token="<OOV>"
)

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

X = pad_sequences(
    sequences,
    maxlen=20,
    padding="post"
)

# -----------------------------
# Label Encoding
# -----------------------------
encoder = LabelEncoder()

y = encoder.fit_transform(labels)

# -----------------------------
# Build Model
# -----------------------------
model = Sequential()

model.add(
    Embedding(
        input_dim=5000,
        output_dim=64
    )
)

model.add(
    LSTM(64)
)

model.add(
    Dense(
        64,
        activation="relu"
    )
)

model.add(
    Dense(
        len(encoder.classes_),
        activation="softmax"
    )
)

# -----------------------------
# Compile
# -----------------------------
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Train
# -----------------------------
model.fit(
    X,
    y,
    epochs=300,
    verbose=1
)

# -----------------------------
# Save Model
# -----------------------------
model.save("model/chatbot_model.keras")

with open("model/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("\n===================================")
print("✅ Training Completed Successfully")
print("✅ chatbot_model.keras Saved")
print("✅ tokenizer.pkl Saved")
print("✅ label_encoder.pkl Saved")
print("===================================")