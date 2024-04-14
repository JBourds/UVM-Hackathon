from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import FieldList, FileField, FormField, StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    title = StringField("Question Title", validators=[DataRequired()], render_kw={"placeholder": "Print \"Hello world!\""})
    prompt = StringField("Question Prompt", validators=[DataRequired()], render_kw={"placeholder": "Write a function to display a \"Hello world!\" message."})
    test_file = FileField("Tests File", validators=[
        FileRequired(),
        FileAllowed(["py"], message="upload .py inputs file")
    ], render_kw={"class": "file_upload"})
    template_file = FileField("Template File (for users)", validators=[
        FileRequired(),
        FileAllowed(["py"], message="upload .py template file")
    ], render_kw={"class": "file_upload"})
    submit = SubmitField("Submit Question", validators=[DataRequired()], render_kw={"style": "margin-top: 1em;"})

class ProblemForm(FlaskForm):
    user_code = TextAreaField("User Code", render_kw={"rows": 10, "style": "font-size: 30px;"})
    submit = SubmitField("Submit")
