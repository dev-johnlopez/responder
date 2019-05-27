from flask import render_template, redirect, g
from flask_security import current_user, login_required
from app import db
from app.views import errors_bp as bp
from app.forms.search import SearchForm

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.errorhandler(403)
def page_forbiden(error):
    return redirect(url_for_security("login"))

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
