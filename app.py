from flask import Flask, render_template,redirect,url_for,request
from models import films
from forms import FilmForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/")
def start():
    return redirect(url_for("films_list"))

@app.route("/films", methods=["GET", "POST"])
def films_list():
    form = FilmForm()
    error = ""
    if request.method == "POST":
      if form.validate_on_submit():
             films.create(form.data)
             films.save_all()
             return redirect(url_for("films_lib"))
    return render_template("films_lib.html", form= FilmForm,films=films.all(), error=error)


# @app.route("/api/v1/films/<int:film_id>", methods=["GET", "POST"])
# def film_details(film_id):
#     film = films.get(film_id - 1)
#     form = FilmForm(data=film)
#
#     if request.method == "POST":
#         if form.validate_on_submit():
#             films.update(film_id - 1, form.data)
#         return redirect(url_for("films_list"))
#     return render_template("films_lib.html", form=form, film_id=film_id)


if __name__ == "__main__":
    app.run(debug=True)

