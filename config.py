import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(base_dir, 'app.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['a.jabed.bd@gmail.com']
    
    
    
# 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': '58c8a2d4be2a81e7d32d3a284c6846afed9d91d4310aeeaf6a39fa35945a6e87', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093, 'ADMINS': ['a.jabed.bd@gmail.com'], 'MAIL_PASSWORD': '$2019@kiB11#', 'MAIL_PORT': 587, 'MAIL_SERVER': 'smtp.googlemail.com', 'MAIL_USERNAME': 'a.jabed.bd@gmail.com', 'MAIL_USE_TLS': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:////home/akib-jabed/Workspace/microblog/app.db', 'SQLALCHEMY_ENGINE_OPTIONS': {}, 'SQLALCHEMY_ECHO': False, 'SQLALCHEMY_BINDS': {}, 'SQLALCHEMY_RECORD_QUERIES': False, 'SQLALCHEMY_TRACK_MODIFICATIONS': False