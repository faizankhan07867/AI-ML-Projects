import zipfile
from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# -------------------------------
# Project Paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "model"

MODEL_DIR.mkdir(exist_ok=True)

FAKE_ZIP = DATASET_DIR / "Fake.csv"
TRUE_ZIP = DATASET_DIR / "True.csv"

# -------------------------------
# Check Files
# -------------------------------

if not FAKE_ZIP.exists():
    raise FileNotFoundError(f"{FAKE_ZIP} not found")

if not TRUE_ZIP.exists():
    raise FileNotFoundError(f"{TRUE_ZIP} not found")

# -------------------------------
# Function to Read CSV from ZIP
# -------------------------------

def read_csv_from_zip(zip_path):
    with zipfile.ZipFile(zip_path, "r") as z:
        csv_files = [f for f in z.namelist() if f.lower().endswith(".csv")]

        if len(csv_files) == 0:
            raise Exception(f"No CSV found inside {zip_path.name}")

        with z.open(csv_files[0]) as file:
            return pd.read_csv(file)

# -------------------------------
# Load Dataset
# -------------------------------

print("Loading datasets...")

fake = read_csv_from_zip(FAKE_ZIP)
true = read_csv_from_zip(TRUE_ZIP)

print("Datasets Loaded Successfully")

# -------------------------------
# Labels
# -------------------------------

fake["label"] = 0
true["label"] = 1

# -------------------------------
# Merge
# -------------------------------

data = pd.concat([fake, true], ignore_index=True)

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# -------------------------------
# Features
# -------------------------------

X = data["text"]
y = data["label"]

# -------------------------------
# Vectorizer
# -------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=50000
)

X = vectorizer.fit_transform(X)

# -------------------------------
# Train Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Model
# -------------------------------

model = LogisticRegression(max_iter=1000)

print("Training Model...")

model.fit(X_train, y_train)

# -------------------------------
# Accuracy
# -------------------------------

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print(f"\nAccuracy : {accuracy*100:.2f}%")

# -------------------------------
# Save
# -------------------------------

joblib.dump(model, MODEL_DIR / "model.pkl")
joblib.dump(vectorizer, MODEL_DIR / "vectorizer.pkl")

print("\nModel Saved Successfully")
print("Training Complete")