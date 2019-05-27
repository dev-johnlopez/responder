from flask import g, render_template, request, redirect, g
from flask_security import current_user, login_required
from app import db
from app.views import deals_bp as bp
from app.forms.search import SearchForm

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('deals/index.html',
                title='Deals')

@bp.route('/opportunities', methods=['GET', 'POST'])
@login_required
def opportunities():
    return render_template('deals/index.html',
                title='Opportunities')

@bp.route('/active', methods=['GET', 'POST'])
@login_required
def active():
    return render_template('deals/index.html',
                title='Active Deals')
