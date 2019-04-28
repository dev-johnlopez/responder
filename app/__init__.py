import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, redirect
from config import Config
from werkzeug.contrib.fixers import ProxyFix
from sendgrid import SendGridAPIClient
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, current_user


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
security = Security()
sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views import email_bp, errors_bp, crm_bp
    app.register_blueprint(email_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(crm_bp, url_prefix="/crm")

    from app.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app=app, datastore=user_datastore)

    #from app.admin import create_admin
    #admin = create_admin(app, db)

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/assignably.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Assignably startup')

    return app
