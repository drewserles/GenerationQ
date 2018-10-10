from flask_wtf import FlaskForm
import wtforms #import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class GenerateForm(FlaskForm):
    area_text = wtforms.TextAreaField('Area Text', validators=[DataRequired()])
    submit = wtforms.SubmitField('Generate!')
