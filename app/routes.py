from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm, EditProfileForm, EmptyForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        

@app.get("/")
@app.get("/index")
@login_required
def index():
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
    return render_template("index.html", title="Home", posts=posts)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    posts = [
        {
            "author": user,
            "body": "This is post 01"
        },
        {
            "author": user,
            "body": "This is post 02"
        }
    ]
    return render_template("user.html", user=user, form=form, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Credentials")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("User Registration Successful!!")
        return redirect(url_for('login'))
    return render_template('register.html', title="Sign Up", form=form)


@app.route('/edit_profile', methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Profile has been updated")
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title="Edit Profile", form=form)

@app.route('/follow/<username>', methods=['POST'])
@app.login_required
def follow_user(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(f"User {username} not found")
            return redirect(url_for('index'))
        if user == current_user:
            flash("You cannot follow yourself!!")
            return redirect(url_for('index'))
        current_user.follow(user)
        db.session.commit()
        flash(f"You are following {username}!!")
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    
@app.route('/unfollow/<username>', methods['POST'])
@login_required
def unfollow_user(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(f"User {username} not found")
            return redirect(url_for('index'))
        if user == current_user:
            flash("You cannot unfollow yourself!!")
            return redirect(url_for('index'))
        current_user.unfollow(user)
        db.session.commit()
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))