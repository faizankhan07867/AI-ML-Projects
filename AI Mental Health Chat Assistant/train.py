import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Create model folder
os.makedirs("model", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/mental_health.csv")

print(df.head())

X = df["text"].astype(str)
y = df["label"].astype(str)

# Vectorization
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X, y)

# Save model
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\n✅ Model Trained Successfully")
print("✅ sentiment_model.pkl Saved")
print("✅ vectorizer.pkl Saved")