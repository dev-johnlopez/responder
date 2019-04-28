from app import db
from app.models.mixins import AuditMixin
from app.constants import TEMPLATE

class Template(db.Model, AuditMixin):
    __tablename__ = 'campaign'
    id = db.Column(db.Integer, primary_key=True)
    touches = db.relationship("TouchPoint", back_populates="template")
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    type = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity':TEMPLATE.UNKNOWN,
        'polymorphic_on':type
    }

    def __repr__(self):
        return "{} {}".format(self.name)

    def __str__(self):
        return "{} {}".format(self.name)

class DirectMailTemplate(Template):

    __mapper_args__ = {
        'polymorphic_identity':TEMPLATE.DIRECT_MAIL
    }

    def __init__(self, **kwargs):
        super(DirectMailTemplate, self).__init__(**kwargs)

class EmailTemplate(Template):

    __mapper_args__ = {
        'polymorphic_identity':TEMPLATE.EMAIL
    }

    def __init__(self, **kwargs):
        super(EmailTemplate, self).__init__(**kwargs)

class TextMessageTemplate(Template):

    __mapper_args__ = {
        'polymorphic_identity':TEMPLATE.TEXT_MESSAGE
    }

    def __init__(self, **kwargs):
        super(TextMessageTemplate, self).__init__(**kwargs)
