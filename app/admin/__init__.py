from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, helpers, expose
from flask_admin.model import BaseModelView
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from redis import Redis
from flask_admin.contrib import rediscli
from app.models import *

def create_admin(app, db):
    admin = Admin(app, name='Assignably', index_view=MyAdminIndexView(), template_mode='bootstrap3')
    admin.add_view(MyModelView(Contact, db.session))
    admin.add_view(MyModelView(Account, db.session))
    #admin.add_view(MyModelView(Deal, db.session))
    #admin.add_view(MyModelView(Property, db.session))
    #admin.add_view(MyModelView(PropertyContact, db.session))
    #admin.add_view(MyModelView(Address, db.session))
    #admin.add_view(MyModelView(Note, db.session))
    admin.add_view(MyModelView(User, db.session))
    #admin.add_view(MyModelView(Role, db.session))
    #admin.add_view(MyModelView(Task, db.session))
    admin.add_view(MyModelView(Tag, db.session))
    admin.add_view(MyModelView(Indicator, db.session))
    #admin.add_view(MyModelView(FairMarketRent, db.session))
    #admin.add_view(MyModelView(Campaign, db.session))
    #admin.add_view(MyModelView(ExternalAccount, db.session))
    admin.add_view(rediscli.RedisCli(Redis()))
    return admin

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        if not current_user.is_authenticated:
            next=url_for(request.endpoint,**request.view_args)
            return redirect(url_for('security.login', next=next))
        abort(403)


# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        next=url_for(request.endpoint,**request.view_args)
        if not current_user.is_authenticated:
            return redirect(url_for('security.login', next=next))
        if not current_user.is_admin():
            return redirect(url_for('security.login', next=next))
        return super(MyAdminIndexView, self).index()
