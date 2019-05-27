from app import db
from flask import current_app, flash
from sqlalchemy import event
from app.services.sendgrid import post_whitelabel_domain, delete_whitelabel_domain, validate_whitelabel_domain


# Define an Account model
class Account(db.Model):

    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship("User", back_populates="account")
    domains = db.relationship("Domain")

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

    def __repr__(self):
        return "{}".format(self.name)

    def addDomain(self, domain):
        if self.domains is None:
            self.domains = []
        self.domains.append(domain)

# Define an Account model
class Domain(db.Model):

    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    sendgrid_domain_id = db.Column(db.Integer)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    domain = db.Column(db.String(255))
    subdomain = db.Column(db.String(255))
    valid = db.Column(db.Boolean)
    dns_records = db.relationship("DNS")

    def __init__(self, **kwargs):
        super(Domain, self).__init__(**kwargs)

    def addDNSRecord(self, record):
        if self.dns_records is None:
            self.dns_records = []
        self.dns_records.append(record)

    def postDomainToSendgrid(self):
        data = post_whitelabel_domain(self.domain)
        self.sendgrid_domain_id = data['id']
        for item in data["dns"]:
            dns = DNS(record_type=item,valid=False,type=data["dns"][item]["type"],host=data["dns"][item]["host"],data=data["dns"][item]["data"])
            self.addDNSRecord(dns)

    def validate(self):
        data = validate_whitelabel_domain(self.sendgrid_domain_id)
        self.valid = data["valid"]
        for item in data["validation_results"]:
            dns = self.getDNSRecordByRecordType(item)
            if dns is not None:
                dns.valid = data["validation_results"][item]["valid"]

    def getDNSRecordByRecordType(self, record_type):
        for dns in self.dns_records:
            if dns.record_type == record_type:
                return dns
        return None


    def delete(self):
        delete_whitelabel_domain(self.sendgrid_domain_id)


# Define an Account model
class DNS(db.Model):

    __tablename__ = 'dns'

    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    record_type = db.Column(db.String(255))
    valid = db.Column(db.Boolean)
    type = db.Column(db.String(255))
    host = db.Column(db.String(255))
    data = db.Column(db.String(255))

    def __init__(self, **kwargs):
        super(DNS, self).__init__(**kwargs)

def delete_domain(mapper, connection, target):
    target.delete()

event.listen(Domain, 'before_delete', delete_domain)
