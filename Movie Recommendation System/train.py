import os
import ast
import pickle
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ===========================
# Load Dataset
# ===========================
movies = pd.read_csv("dataset/movies.csv")

print("Dataset Loaded Successfully")
print(movies.head())
print("\nColumns:")
print(movies.columns.tolist())


# ===========================
# Select Required Columns
# ===========================
required_columns = [
    "movie_id",
    "title",
    "overview",
    "genres",
    "keywords",
    "cast",
    "crew"
]

movies = movies[required_columns]

movies.dropna(inplace=True)


# ===========================
# Convert JSON String to List
# ===========================
def convert(text):
    L = []
    try:
        for i in ast.literal_eval(text):
            L.append(i["name"])
    except:
        pass
    return L


movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)


# ===========================
# Top 3 Cast Members
# ===========================
def convert_cast(text):
    L = []
    try:
        counter = 0
        for i in ast.literal_eval(text):
            if counter < 3:
                L.append(i["name"])
                counter += 1
            else:
                break
    except:
        pass
    return L


movies["cast"] = movies["cast"].apply(convert_cast)


# ===========================
# Director
# ===========================
def fetch_director(text):
    L = []
    try:
        for i in ast.literal_eval(text):
            if i["job"] == "Director":
                L.append(i["name"])
                break
    except:
        pass
    return L


movies["crew"] = movies["crew"].apply(fetch_director)


# ===========================
# Process Overview
# ===========================
movies["overview"] = movies["overview"].apply(lambda x: x.split())


# ===========================
# Remove Spaces
# ===========================
for feature in ["genres", "keywords", "cast", "crew"]:
    movies[feature] = movies[feature].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )


# ===========================
# Create Tags
# ===========================
movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)


# ===========================
# Final DataFrame
# ===========================
new_df = movies[["movie_id", "title", "tags"]].copy()

new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x).lower())


# ===========================
# Vectorization
# ===========================
cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(new_df["tags"]).toarray()


# ===========================
# Similarity Matrix
# ===========================
similarity = cosine_similarity(vectors)


# ===========================
# Save Models
# ===========================
os.makedirs("model", exist_ok=True)

pickle.dump(new_df, open("model/movies.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))


print("\n======================================")
print("Training Completed Successfully")
print("Movies:", len(new_df))
print("Saved:")
print("model/movies.pkl")
print("model/similarity.pkl")
print("======================================")