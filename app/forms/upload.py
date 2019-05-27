from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, FormField, BooleanField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Optional
from app.models import Tag
from app.forms.tag import TagForm
from app.forms.indicator import IndicatorForm

class OptionsForm(FlaskForm):
    is_seller = BooleanField("Seller", validators=[Optional()])
    is_investor = BooleanField("Seller", validators=[Optional()])
    is_wholesaler = BooleanField("Seller", validators=[Optional()])
    is_broker = BooleanField("Seller", validators=[Optional()])
    is_property_manager = BooleanField("Seller", validators=[Optional()])
    is_developer = BooleanField("Seller", validators=[Optional()])
    #tags = FieldList(FormField(TagForm))
    #indicators = FieldList(FormField(IndicatorForm))

class UploadForm(FlaskForm):
    file = FileField(validators=[
        FileRequired(),
        FileAllowed(['xls', 'xlsx', 'csv'], 'CSV/Excel only!')
    ])
    options = FormField(OptionsForm)
