from flask import g, render_template, redirect, url_for
from app import db
from app.models import Contact
from app.views import dashboard_bp as bp
from app.forms import ContactForm

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/dashboard', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('dashboard/index.html',
                title='Dashboard')
