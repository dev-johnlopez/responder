from flask import g, render_template, request, redirect
from app import db
from app.views import deals_bp as bp

@bp.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('deals/index.html',
                title='Deals')

@bp.route('/opportunities', methods=['GET', 'POST'])
def opportunities():
    return render_template('deals/index.html',
                title='Opportunities')

@bp.route('/active', methods=['GET', 'POST'])
def active():
    return render_template('deals/index.html',
                title='Active Deals')
