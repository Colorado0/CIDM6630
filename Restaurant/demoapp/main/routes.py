from flask import Blueprint, request, flash, redirect, render_template, url_for, jsonify
from demoapp.models import Customer
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from demoapp import db


class signupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/signup")
def signup():
    print("Made it here")
    form = signupForm()
    if request.method == "POST":
        print("post request")
        if form.validate_on_submit():
            print("form validated")
            # date_added = "2021/03/17"
            # bookmark = Bookmarks(title=form.title.data,
            #                      url=form.url.data, notes=form.notes.data, date_added=date_added)
            # db.session.add(bookmark)
            # db.session.commit()
            # print("data added to db")
            # print(bookmark)
            # flash('Your bookmark has been created!', 'success')
            # return redirect(url_for('main.base'))
        else:
            print(form.errors)
    return render_template('signup.html',
                           form=form)


@main.route("/customers")
def customers():
    e = Customer.query.all()
    print(e)
    return "success"


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
