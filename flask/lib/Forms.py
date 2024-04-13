from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class AdminForm(FlaskForm):
    title = StringField("Title")
    prompt = StringField("Prompt")
    template = TextAreaField("Template Code")
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    user_code = TextAreaField("User Code")
    submit = SubmitField("Submit")

