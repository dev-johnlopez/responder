from flask import g, render_template, request, redirect
from app import db
from app.views import marketing_bp as bp

@bp.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('marketing/index.html',
                title='Marketing')

@bp.route('/campaigns', methods=['GET', 'POST'])
def campaigns():
    return render_template('marketing/index.html',
                title='Marketing')

@bp.route('/sequences', methods=['GET', 'POST'])
def sequences():
    return render_template('marketing/index.html',
                title='Marketing')
