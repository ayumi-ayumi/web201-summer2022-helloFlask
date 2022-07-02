from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class SampleForm(FlaskForm):
    userName = StringField('Your name', validators=[DataRequired(), Length(min=1, max=4)])
    userAge = IntegerField('Your Age', validators=[DataRequired()])

    submit = SubmitField('Submit')