from flask import Flask, render_template, redirect, url_for, request
from models import films
from forms import FilmForm
from wtforms import SubmitField
import json
app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/")
def start():
    return redirect(url_for("films_list"))

#view all records/add record
@app.route("/api/v1/films/", methods=["GET", "POST"])
def films_list():
    form = FilmForm()
    form.id.data = films.get(-1)['id']
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            films.create(form.data)
            films.save_all()
            return redirect(url_for("films_list"))  # go back to films database
    return render_template("films_lib.html", form=form, films=films.all(), error=error)


# view/change/delete
@app.route("/api/v1/films/<int:film_id>", methods=["GET", "POST","DELETE"])
def film_details(film_id):
    film = films.get(film_id - 1)
    form = FilmForm(data=film)
    if form.validate_on_submit():
       if request.form['submit_button'] == 'Change':
          films.update(film_id - 1, form.data)
          print("changed")
          return redirect(url_for("films_list"))  # after update go back to films database
       if request.form['submit_button'] == 'Delete':

           result = films.delete(film_id-1)
           if not result:
                abort(404)
           return redirect(url_for("films_list"))

       elif request.form['submit_button'] == 'Go Back':
            print("back")
            return redirect(url_for("films_list"))  # after update go back to films database
    # film_details html for change
    return render_template("film_details.html", form=form, film_id=film_id)



if __name__ == "__main__":
    app.run(debug=True)
