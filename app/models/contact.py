from app import db
from app.models.mixins import AuditMixin
from app.models.mixins import SearchableMixin

class Contact(db.Model, AuditMixin, SearchableMixin):
    __tablename__ = 'contact'
    __searchable__ = ['first_name', 'last_name', 'phone']
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def getMotivationIndicators(self):
        return [
            "Probate",
            "Foreclosure",
            "Short Sale",
            "Estate Sale",
            "Divorce",
            "Absentee Owner",
            "Recent Eviction",
            "Senior Citizen",
            "High Equity"
        ]
