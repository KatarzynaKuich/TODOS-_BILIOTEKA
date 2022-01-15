from flask import Flask, jsonify, make_response, request, abort
from forms import FilmForm
from models import films

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


# error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


# view all records
@app.route("/api/v1/films/", methods=["GET"])
def films_api():
    return jsonify(films.all())


# view
@app.route("/api/v1/films/<int:film_id>", methods=["GET"])
def film_details(film_id):
    try:
        film = films.get(film_id - 1)
    except IndexError:
        film = 'null'
        abort(404)
    return jsonify({"film": film})


# add record
@app.route("/api/v1/films/", methods=["POST"])
def films_create():
    if not request.json:
        abort(400)  # go to errorhandler
    return jsonify({"film": film}), 201


# delete
@app.route("/api/v1/films/<int:film_id>", methods=['DELETE'])
def delete_film(film_id):
    try:
        result = films.delete(film_id - 1)
    except IndexError:
        result = 'null'
        abort(404)
    return jsonify({'result': result})


# change
@app.route("/api/v1/films/<int:film_id>", methods=["PUT"])
def update_film(film_id):
    film = films.get(film_id)
    if not film:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([

        "id" in data and not isinstance(data.get('id'), int),
        "title" in data and not isinstance(data.get('title'), str),
        "plot" in data and not isinstance(data.get('plot'), str),
        "year" in data and not isinstance(data.get('year'), str),
        "actors" in data and not isinstance(data.get('actors'), str),
        "posterUrl" in data and not isinstance(data.get('posterUrl'), str),
        "genres" in data and not isinstance(data.get('title'), str)
    ]):
        abort(400)
    film = {
        "id": data.get('id', film['id']),
        "title": data.get('title', film['title']),
        "plot": data.get('plot', film['plot']),
        "year": data.get('year', film['year']),
        "actors": data.get('actors', film['actors']),
        "posterUrl": data.get('posterUrl', film['posterUrl']),
        "genres": data.get('genres', film['genres'])
    }
    films.updateAPI(film_id, film)
    return jsonify({'film': film})


if __name__ == "__main__":
    app.run(debug=True)
