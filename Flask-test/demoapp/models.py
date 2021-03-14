from datetime import datetime
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from demoapp import db


class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    url = db.Column(db.String(64), unique=True, nullable=False)
    notes = db.Column(db.String(120), unique=True, nullable=False)
    date_added = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Bookmarks('{self.title}', '{self.url}')"
