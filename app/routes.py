from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.get("/")
@app.get("/index")
def index():
    user = {"username": "Akib-Jabed"}
    posts = [
        {
            "author": {"username": "Akib-Jabed"},
            "body": "This is post 01"
        },
        {
            "author": {"username": "Akib-Jabed"},
            "body": "This is post 02"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)