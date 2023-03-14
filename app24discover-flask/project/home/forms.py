from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField(
        'Description', validators=[DataRequired(), Length(max=140)])
