from flask import g, render_template, redirect, url_for, g
from flask_security import current_user, login_required
from app import db
from app.models import Contact
from app.views import dashboard_bp as bp
from app.forms import ContactForm
from app.forms.search import SearchForm

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/dashboard', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('dashboard/index.html',
                title='Dashboard')
