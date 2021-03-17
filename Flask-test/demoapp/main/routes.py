from flask import Blueprint, request, flash, redirect, render_template, url_for, jsonify
from demoapp.models import Bookmarks
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from demoapp import db


class BookmarkForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')


main = Blueprint('main', __name__)


@main.route("/")
def base():
    return "home"


@main.route("/bookmarks")
def bookmarks():
    e = Bookmarks.query.all()
    print(e)
    return jsonify(e)


@main.route("/addbookmark", methods=["GET", "POST"])
def addbookmark():
    print("Made it here")
    form = BookmarkForm()
    if request.method == "POST":
        print("post request")
        if form.validate_on_submit():
            print("form validated")
            date_added = "2021/03/17"
            bookmark = Bookmarks(title=form.title.data,
                                 url=form.url.data, notes=form.notes.data, date_added=date_added)
            db.session.add(bookmark)
            db.session.commit()
            print("data added to db")
            print(bookmark)
            flash('Your bookmark has been created!', 'success')
            return redirect(url_for('main.base'))
        else:
            print(form.errors)
    return render_template('create_bookmark.html',
                           form=form)
