from flaskblog.views.users.routes import users
from flaskblog.views.main.routes import main
from flaskblog.views.posts.routes import posts
from flaskblog.views.errors.handlers import errors

blueprints = [users, main, posts, errors]
