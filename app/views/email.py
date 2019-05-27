from flask import g, render_template, request, redirect, g, flash
from flask_security import current_user, login_required
from app import db
from app.views import email_bp as bp
from app.forms.email import EmailForm
from app.services.sendgrid import send_mail
from app.forms.search import SearchForm


@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    form = EmailForm()
    if form.validate_on_submit():
        send_mail(form.to_email.data, form.subject.data, form.body.data,from_email=current_user.email)
        if request.args.get('next') is not None:
            return redirect(request.args.get('next'))
    else:
        if request.args.get('to') is not None:
            form.to_email.data = request.args.get('to')
    return render_template('email/compose.html',
                title='Compose Email',
                form=form)
