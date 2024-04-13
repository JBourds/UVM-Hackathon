"""
flask/app.py

Description: Flask app running as the web app.
Author:      Jordan Bourdeau, Noah Schonhorn
Date:        4/13/24
"""

from flask import Flask, jsonify, redirect, render_template, request, Response
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.inspection import inspect
from flask_wtf import CSRFProtect, FlaskForm, csrf
from pprint import pprint

import json
import os
from lib.Forms import AdminForm, UserForm

app = Flask(__name__)
boostrap = Bootstrap5(app)
csrf = CSRFProtect(app)
basedir: str = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(basedir, "database.db")
db = SQLAlchemy()

class Tutorial(db.Model):
    order = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    prompt = db.Column(db.Text)
    language = db.Column(db.String(64))
    template_code = db.Column(db.Text)
    test_code = db.Column(db.Text)
    test_inputs = db.Column(db.Text)    # Pickled array of potential array inputs

    @staticmethod
    def get_pickled_oracle_function(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['test_code']
    
    @staticmethod
    def get_template_code(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['template_code']
    
    @staticmethod
    def get_pickled_test_inputs(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['test_inputs']
    
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

@app.route("/admin", methods=["GET"])
def admin():
    form = AdminForm(meta={'csrf': False})
    return render_template("admin.html", form=form)

@app.route("/check_question", methods=["POST"])
@csrf.exempt
def check_question():

    return redirect("/user", code=302)

@app.route("/problem/<id>", methods=["GET"])
@csrf.exempt
def problem(id: int):
    template_code: str = Tutorial.get_template_code(id)
    output: str = request.args.get("output", "Output will show here once you run your code")
    code_analysis: str = request.args.get("code_analysis", "Code analysis will show here once you run your code")

    form = UserForm(meta={'csrf': False})
    form.template.data = template_code
    return render_template("user.html", form=form, output=output, code_analysis=code_analysis)


if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    # Create all the tables
    with app.app_context():
        db.create_all()

        # Test code
        tutorial = Tutorial(name="Test", prompt="Test", language="Python", template_code="def test_", test_code="test code", test_inputs="test input")
        db.session.add(tutorial)    
        tutorial2 = Tutorial(name="Test", prompt="Test", language="Python", template_code="def test_", test_code="test code", test_inputs="test input")
        db.session.add(tutorial2)    
        db.session.commit()

    app.run(port=5000, debug=True)
