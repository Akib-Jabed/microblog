import random, os
from flask_mail import Message
from flask import url_for, current_app
from flaskblog import mail



def save_image(from_picture):
    random_key = str(random.random()).split('.')[1]
    _, file_ext = os.path.splitext(from_picture.filename)
    picture_filename = random_key + file_ext
    filename = os.path.join(current_app.root_path, 'static/pro_pics/', picture_filename)
    from_picture.save(filename)
    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='sender@gmail.com',   #use valid email else gmail refuse the sender
                  recipients=[user.email])
    msg.body = '''To reset your password, visit the following link:
{}
If you did not make this request then simply ignore this email and no changes will be made.
'''.format(url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)
