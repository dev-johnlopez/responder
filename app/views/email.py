from flask import g, render_template, request, redirect
from app import db
from app.views import email_bp as bp
from app.forms.email import EmailForm
from app.services import sg_mail as sendgrid

@bp.route('/compose', methods=['GET', 'POST'])
def compose():
    form = EmailForm()
    if form.validate_on_submit():
        print("*****")
        sendgrid.send_mail(form.to_email.data, form.subject.data, form.body.data)
        return redirect(request.args.get('next'))
    else:
        form.to_email.data = request.args.get('to')
    return render_template('email/compose.html',
                title='Compose Email',
                form=form)
