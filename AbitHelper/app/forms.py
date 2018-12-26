from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class SpecialityForm(FlaskForm):
    specialities = SelectField('Speciality', coerce=int)
    mark = DecimalField('Mark', validators=[DataRequired()])
    submit = SubmitField('Submit')


    def validate_mark(form, field):
        if field.data<100 or field.data>200:
            raise ValidationError('Mark must be from 100 to 200')

