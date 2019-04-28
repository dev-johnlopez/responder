from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FormField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    to_email = StringField('To', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    html_content = StringField('Text', validators=[DataRequired()])
