from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,URLField,DateField

class FilmForm(FlaskForm):
    id =StringField()
    title   = StringField()
    plot    = TextAreaField()
    year    = DateField()
    actors = TextAreaField()
    posterUrl= StringField()

