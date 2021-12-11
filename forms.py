from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,URLField,IntegerField,SubmitField
from wtforms.validators import DataRequired,NumberRange,Length
class FilmForm(FlaskForm):
    id =      StringField()
    title   = StringField()
    plot    = TextAreaField()
    year    = StringField()
    actors = StringField()
    posterUrl= StringField()
    genres = StringField()


