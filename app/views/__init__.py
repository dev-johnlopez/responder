from flask import Blueprint

email_bp = Blueprint('email', __name__)

from . import email

errors_bp = Blueprint('errors', __name__)

from . import errors

crm_bp = Blueprint('crm', __name__)

from . import crm

dashboard_bp = Blueprint('dashboard', __name__)

from . import dashboard

marketing_bp = Blueprint('marketing', __name__)

from . import marketing

deals_bp = Blueprint('deals', __name__)

from . import deals
