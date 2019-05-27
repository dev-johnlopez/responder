from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FormField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from app.constants import template

class TemplateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    type = SelectField('Type', choices=[
                                    ("",""),
                                    ("1","Email")],
                                validators=[DataRequired()])
