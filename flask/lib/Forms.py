from flask_bootstrap import BooleanField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import FieldList, FileField, FormField, StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    prompt = StringField("prompt", validators=[DataRequired()])
    # template = TextAreaField("template", default="# enter code here", validators=[DataRequired()])
    test_file = FileField("test file", validators=[
        FileRequired(),
        FileAllowed(["py"], message="upload .py inputs file")
    ])
    template_file = FileField("template file", validators=[
        FileRequired(),
        FileAllowed(["py"], message="upload .py template file")
    ])
    submit = SubmitField("submit", validators=[DataRequired()])

class ProblemForm(FlaskForm):
    user_code = TextAreaField("User Code")
    submit = SubmitField("Submit")
