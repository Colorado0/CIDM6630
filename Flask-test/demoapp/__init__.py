
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """ Create the flask app instance"""

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///bookmarks.db'
    db.init_app(app)

    from demoapp.main.routes import main

    app.register_blueprint(main)

    return app
