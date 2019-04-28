import os
from flask import flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to_emails, subject, html_content):
    message = Mail(
        from_email=os.environ.get('SENDGRID_DEFAULT_FROM'),#'john@johnlopez.org',#str(os.environ.get('SENDGRID_DEFAULT_FROM')),
        to_emails=str(to_emails),
        subject=str(subject),
        html_content=str(html_content))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        flash('Sent!', 'success')
    except Exception as e:
        flash(str(e),'error')
