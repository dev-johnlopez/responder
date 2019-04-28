from app import db
from app.models.mixins import AuditMixin

class Campaign(db.Model, AuditMixin):
    __tablename__ = 'campaign'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    touches = db.relationship("TouchPoint", back_populates="campaign")

    def __repr__(self):
        return "{} {}".format(self.name)

    def __str__(self):
        return "{} {}".format(self.name)

class TouchPoint(db.Model, AuditMixin):
    __tablename__ = 'campaign'
    id = db.Column(db.Integer, primary_key=True)
    campagin_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    campaign = db.relationship("Campaign", back_populates="touches")
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'))
    template = db.relationship("Template", back_populates="touches")
    send_date = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean)


    def __repr__(self):
        return "{} {}".format(self.name)

    def __str__(self):
        return "{} {}".format(self.name)
