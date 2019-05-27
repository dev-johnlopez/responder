import os
import json
from flask import flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to_emails, subject, html_content, from_email=os.environ.get('SENDGRID_DEFAULT_FROM')):
    message = Mail(
        from_email=str(from_email),
        to_emails=str(to_emails),
        subject=str(subject),
        html_content=str(html_content))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        flash('Mail Sent!', 'success')
    except Exception as e:
        flash(str(e),'error')

def post_whitelabel_domain(domain, username="", automatic_security=True, custom_spf=False, default=False):
    data = {
      "automatic_security": automatic_security,
      "custom_spf": custom_spf,
      "default": default,
      "domain": domain,
      "username": username
    }
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.client.whitelabel.domains.post(request_body=data)
    return json.loads(response.body)

def validate_whitelabel_domain(domain_id):
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.client.whitelabel.domains._(domain_id).validate.post()
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return json.loads(response.body)

def delete_whitelabel_domain(domain_id):
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.client.whitelabel.domains._(domain_id).delete()
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return json.loads(response.body)
    except Exception as e:
        pass

def create_sendgrid_user():
    data = {
      "automatic_security": False,
      "custom_spf": True,
      "default": True,
      "domain": "example.com",
      "ips": [
        "192.168.1.1",
        "192.168.1.2"
      ],
      "subdomain": "news",
      "username": "john@example.com"
    }
    response = sg.client.whitelabel.domains.post(request_body=data)
    pass
