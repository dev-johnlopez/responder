from app import db
from app.mixins.audit import AuditMixin
from app.mixins.searchable import SearchableMixin

class Contact(db.Model, AuditMixin, SearchableMixin):
    __tablename__ = 'contact'
    __searchable__ = ['first_name', 'last_name', 'phone']
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
