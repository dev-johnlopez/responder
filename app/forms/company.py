from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CompanyForm(FlaskForm):
    name = StringField('Company Name', validators=[DataRequired()])
