from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class TestForm(FlaskForm):
    title = StringField("title")
    language = StringField("language")
    prompt = StringField("prompt")
    template = TextAreaField("# template code")
    submit = SubmitField("submit")
