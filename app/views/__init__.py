from flask import Blueprint

email_bp = Blueprint('email', __name__)

from . import email

errors_bp = Blueprint('errors', __name__)

from . import errors

crm_bp = Blueprint('crm', __name__)

from . import crm
