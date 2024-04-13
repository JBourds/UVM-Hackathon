"""
flask/app.py

Description: Flask app running as the web app.
Author:      Jordan Bourdeau, Noah Schonhorn
Date:        4/13/24
"""

from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
import os
from pprint import pprint

app = Flask(__name__)

basedir: str = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(basedir, "database.db")
db = SQLAlchemy()

def print_and_return(client_bindings: dict) -> Response:
    """
    Description:                Method used to print server response before returning it.
    :param client_bindings:     Dictionary to be jsonifed and sent to the client.
    :return:                    JSON response of dictionary.
    """
    pprint(client_bindings)
    return jsonify(client_bindings)

@app.route('/', methods=["GET"])
def home_page():
    return print_and_return({"Connected": True})


if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    # Create all the tables
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)