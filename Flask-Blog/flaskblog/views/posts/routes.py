from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog.views.posts.forms import PostForm
from flaskblog import db
from flaskblog.models import Post
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        _post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_post.html', title='New Post',
                           form=form, legend='New Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    _post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=_post.title, post=_post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    _post = Post.query.get_or_404(post_id)
    if _post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        _post.title = form.title.data
        _post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=_post.id))
    elif request.method == 'GET':
        form.title.data = _post.title
        form.content.data = _post.content
    return render_template('new_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    _post = Post.query.get_or_404(post_id)
    if _post.author != current_user:
        abort(403)
    db.session.delete(_post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
