from flask import Flask, render_template, request
from recommender import recommend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def movie():

    movie_name = request.form['movie']

    try:
        movies = recommend(movie_name)
        return render_template(
            'index.html',
            recommendations=movies,
            movie=movie_name
        )

    except:
        return render_template(
            'index.html',
            error="Movie Not Found!"
        )

if __name__ == "__main__":
    app.run(debug=True)