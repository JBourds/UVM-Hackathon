"""
flask/app.py

Description: Flask app running as the web app.
Author:      Jordan Bourdeau, Noah Schonhorn
Date:        4/13/24
"""

from flask import Flask, jsonify, render_template, request, Response
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect, FlaskForm, csrf
from pprint import pprint

import os
from lib.Forms import TestForm

app = Flask(__name__)
boostrap = Bootstrap5(app)
csrf = CSRFProtect(app)
basedir: str = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(basedir, "database.db")
db = SQLAlchemy()

class Tutorials(db.Model):
    order = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    prompt = db.Column(db.Text)
    language = db.Column(db.String(64), unique=True)
    template_code = db.Column(db.Text)
    test_code = db.Column(db.Text)
    expected_output = db.Column(db.Text)

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

@app.route("/admin", methods=["GET"])
def admin():
    form = TestForm(meta={'csrf': False})
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
    app.run(port=5000, debug=True)
