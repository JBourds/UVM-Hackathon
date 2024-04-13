"""
flask/app.py

Description: Flask app running as the web app.
Author:      Jordan Bourdeau, Noah Schonhorn
Date:        4/13/24
"""

from re import template
from flask import Flask, jsonify, redirect, render_template, request, Response, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.inspection import inspect
from flask_wtf import CSRFProtect, FlaskForm, csrf
from pprint import pprint

import json
import os
from lib.Forms import AdminForm, ProblemForm

app = Flask(__name__)
boostrap = Bootstrap5(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
csrf_secret_key = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = csrf_secret_key
basedir: str = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(basedir, "database.db")
db = SQLAlchemy()

class Tutorial(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    prompt = db.Column(db.Text)
    template_code = db.Column(db.Text)
    test_code = db.Column(db.Text)

    def __init__(self, name: str, prompt: str, template_code: str, test_code: str):
        self.name = name
        self.prompt = prompt
        self.template_code = template_code
        self.test_code = test_code

    @staticmethod
    def get_oracle_function(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['test_code']
    
    @staticmethod
    def get_template_code(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['template_code']
    
    @staticmethod
    def get_row(problem_number: int):
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()
    
    def serialize(self):
        """
        Description:    Method used to serialize a Table object's properties into JSON format.
        :return:
        """
        return {c: getattr(self, c) for c in inspect(self).attrs.keys() if not c.startswith("_")}
    
    def delete(self) -> None:
        """
        Description:    Method used to delete an object from the database.
        :return:        None.
        """
        db.session.delete(self)


def print_and_return(client_bindings: dict) -> Response:
    """
    Description:             Method used to print server response before returning it.
    :param client_bindings:  Dictionary to be jsonifed and sent to the client.
    :return:                 JSON response of dictionary.
    """
    pprint(client_bindings)
    return jsonify(client_bindings)

# Endpoints
@app.route("/", methods=["GET"])
def main():
    return render_template("base.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/admin", methods=["GET", "POST"])
@csrf.exempt # FIXME: not secure, fix later
def admin():
    form = AdminForm(meta={'csrf': False})
    if form.validate_on_submit():
        data1 = form.test_file.data
        data2 = form.template_file.data

        tests_data_str = ""
        for d in data1:
            tests_data_str += (d.decode("utf-8"))

        templates_data_str = ""
        for d in data2:
            templates_data_str += (d.decode("utf-8"))

        title: str = request.form["title"]
        prompt: str = request.form["prompt"]

        tutorial = Tutorial(name=title, prompt=prompt, template_code=templates_data_str, test_code=tests_data_str)
        db.session.add(tutorial)    
        db.session.commit()

        return redirect(url_for("admin"))
    else:
        return render_template("admin.html", form=form)
    

@app.route("/check_question", methods=["POST"])
@csrf.exempt
def check_question():
    data = request.form
    problem_id: int = data['problem_id']
    user_function: str = data['user_code']
    table_row = Tutorial.get_row(problem_id)
    print(table_row)

    return redirect(f"/problem/{problem_id}", code=302)

@app.route("/problem/<int:id>", methods=["GET"])
@csrf.exempt
def problem(id: int):
    problem_count = db.session.query(func.count(Tutorial.order)).scalar()

    if id > problem_count:
        return redirect(url_for('problem', problem_id=problem_count))

    if id < 1:
        return redirect(url_for('problem', problem_id=1))

    template_code: str = Tutorial.get_template_code(id)

    output: str = request.args.get("output", "Output will show here once you run your code")
    code_analysis: str = request.args.get("code_analysis", "Code analysis will show here once you run your code")

    form = ProblemForm(meta={'csrf': False})
    form.user_code.data = template_code
    return render_template("user.html", form=form, problem_id=id, problem_count=problem_count, output=output, code_analysis=code_analysis)

if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    # Create all the tables
    with app.app_context():
        db.create_all()

        # Test code
        tutorial = Tutorial(name="Test", prompt="Test", template_code="def test_", test_code="test code")
        db.session.add(tutorial)    
        tutorial2 = Tutorial(name="Test", prompt="Test", template_code="def test_", test_code="test code")
        db.session.add(tutorial2)    
        db.session.commit()

    app.run(port=5000, debug=True)
