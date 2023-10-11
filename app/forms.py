from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class CreateArtistForm(FlaskForm):
    name = StringField('Artist Name')
    hometown = StringField('Hometown')
    description = TextAreaField('Description')
    submit = SubmitField('Create New Artist')