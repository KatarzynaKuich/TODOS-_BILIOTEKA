from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,URLField,IntegerField

class FilmForm(FlaskForm):
    id =      IntegerField()
    title   = StringField()
    plot    = TextAreaField()
    year    = StringField()
    actors = TextAreaField()
    posterUrl= StringField()
    genres = StringField()

