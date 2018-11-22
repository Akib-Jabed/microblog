from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import Config
from flask_mail import Mail

db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail()

app = Flask(__name__)

def create_app(config_class=Config):
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from flaskblog.views import blueprints
    from flaskblog.views.main.routes import mainApi

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
