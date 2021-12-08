from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,URLField

class TodoForm(FlaskForm):
    id =StringField()
    title   = StringField()
    plot    = TextAreaField()
    year = StringField()
    actors = TextAreaField()

