from datetime import datetime
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from demoapp import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    date_added = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Customer('{self.name}', '{self.date_added}')"
