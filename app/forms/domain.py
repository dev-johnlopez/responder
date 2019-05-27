from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class DomainForm(FlaskForm):
    domain = StringField('Domain', validators=[DataRequired()])
