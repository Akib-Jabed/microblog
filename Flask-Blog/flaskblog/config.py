import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite3:///blog.db'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL', True))
    #GMAIL MUST BE VALID
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'sample@gmail.com')
    #USE GMAIL APP PASSWORD INSTEAD OF REGULAR PASSWORD
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'gmail_app_password')

