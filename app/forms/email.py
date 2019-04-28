from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FormField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class EmailForm(FlaskForm):
    to_email = StringField('To', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = StringField('Text', widget=TextArea(), validators=[DataRequired()])
