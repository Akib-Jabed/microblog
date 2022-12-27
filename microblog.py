from app import app, db
from app.models import User, Post

# customize the shell context so that after running `flask shell` along with app(Flask Application Instance) the db(Sqlalchemy Instance) and both `User` and `Post` models automatically pre-imported
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}