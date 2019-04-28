from flask import g, render_template
from app import db
from app.views import crm_bp as bp

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('crm/index.html',
                title='CRM')
