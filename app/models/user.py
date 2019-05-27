from app import app, db
from app.models.account import Account
from flask import current_app
from flask_security import UserMixin, user_registered
from app.services.sendgrid import create_sendgrid_user
import json
from time import time

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

# Define a User model
class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship("Account", back_populates="users")
    email = db.Column(db.String(255), unique=True)

    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(40))
    current_login_ip = db.Column(db.String(40))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.account is None:
            self.account = Account()

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def is_admin(self):
        return self.email in current_app.config['ADMINS']
