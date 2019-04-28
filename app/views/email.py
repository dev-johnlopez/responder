from flask import g, render_template
from app import db
from app.views import email_bp as bp
from app.forms.email import EmailForm
from app.services import sg_mail as sendgrid

@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = EmailForm()
    if form.validate_on_submit():
        print("*****")
        sendgrid.send_mail(form.to_email.data, form.subject.data, form.html_content.data)
    return render_template('email/index.html',
                title='Dashboard',
                form=form)
