from flask_wtf import FlaskForm
from wtforms import HiddenField, BooleanField, IntegerField, StringField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Optional

class IndicatorForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    name = StringField('Name', validators=[Optional()])
    enabled = BooleanField('Enabled?', validators=[Optional()])
