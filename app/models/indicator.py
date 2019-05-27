from app import db
from app.models.mixins import AuditMixin

class Indicator(db.Model, AuditMixin):
    __tablename__ = 'Indicator'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __repr__(self):
        return "{}".format(self.name)
