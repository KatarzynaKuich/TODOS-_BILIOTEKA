from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,URLField,IntegerField,SubmitField
from wtforms.validators import DataRequired,NumberRange,Length
class FilmForm(FlaskForm):
    id =      IntegerField(validators=[DataRequired()])
    title   = StringField(validators=[DataRequired()])
    plot    = TextAreaField()
    year    = StringField()
    actors = StringField()
    posterUrl= StringField()
    genres = StringField()


