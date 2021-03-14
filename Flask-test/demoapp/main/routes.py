from flask import Blueprint
from demoapp.models import Bookmarks

main = Blueprint('main', __name__)


@main.route("/")
def base():
    return "home"


@main.route("/bookmarks")
def bookmarks():
    e = Bookmarks.query.all()
    print(e)
    return "hello world"
