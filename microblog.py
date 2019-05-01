from app import create_app, db
from app.models import User, Post, Task, Message, Notification

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user': User, 'post': Post, 'Task': Task,
            'Message': Message, 'Notification': Notification}