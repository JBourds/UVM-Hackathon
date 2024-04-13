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
import os
from flask_wtf import CSRFProtect
from pprint import pprint

from lib.Forms import TestForm

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

    @staticmethod
    def get_pickled_oracle_function(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['test_code']
    
    @staticmethod
    def get_pickled_test_inputs(problem_number: int) -> str:
        return Tutorial.query.filter(Tutorial.order == problem_number).first().serialize()['test_inputs']

    def __init__(self, name: str, prompt: str, template_code: str, test_code: str):
        self.name = name
        self.prompt = prompt
        self.template_code = template_code
        self.test_code = test_code
    
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
    form = TestForm(meta={'csrf': False})
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
    

@app.route("/user", methods=["GET"])
def user():
    return render_template("user.html")


if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    # Create all the tables
    with app.app_context():
        db.create_all()

        # Test code
        # tutorial = Tutorial(name="Test", prompt="Test", language="Python", template_code="def test_", test_code="test code", test_inputs="test input")
        # db.session.add(tutorial)    
        # db.session.commit()
        # print(Tutorial.get_pickled_oracle_function(1))

    app.run(port=5000, debug=True)
