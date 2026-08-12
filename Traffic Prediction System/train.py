import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset/traffic.csv")

X = df.drop("Traffic", axis=1)
y = df["Traffic"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Accuracy :", model.score(X_test, y_test))

joblib.dump(model, "model.pkl")