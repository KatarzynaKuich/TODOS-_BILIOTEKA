import random

from flask import Flask, render_template,redirect,url_for,request
from models import films
from forms import filmForm

app = Flask(__name__)

def get_movies(list_type='popular', how_many=8):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=headers)
    try:
        response.raise_for_status()
    except HTTPError:
        get_movies()
    data = response.json()
    data = random.sample(data['results'], len(data['results']))
    return data[:how_many]


if __name__ == "__main__":
    app.run(debug=True)