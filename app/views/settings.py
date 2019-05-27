from flask import g, render_template, redirect, url_for, flash
from flask_security import current_user, login_required
from app import db
from app.models import Domain, DNS
from app.views import settings_bp as bp
from app.forms.search import SearchForm
from app.forms.domain import DomainForm
from app.forms.profile import ProfileForm
from app.forms.company import CompanyForm
from app.services.sendgrid import post_whitelabel_domain

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CompanyForm(obj=current_user.account)
    if form.validate_on_submit():
        form.populate_obj(current_user.account)
        db.session.add(current_user.account)
        db.session.commit()
    return render_template('settings/index.html',
                title='Account Settings',
                account=current_user.account,
                form=form)

@bp.route('/email', methods=['GET', 'POST'])
@login_required
def email():
    return render_template('settings/email.html',
                title='Email Configuration',
                account=current_user.account)

@bp.route('/add/domains', methods=['GET', 'POST'])
def add_domain():
    form = DomainForm()
    if form.validate_on_submit():
        domain = Domain()
        form.populate_obj(domain)
        #data = post_whitelabel_domain(domain.domain)
        #domain.sendgrid_domain_id = data['id']
        #flash(data, 'info')
        #for item in data["dns"]:
        #    dns = DNS(valid=False,type=data["dns"][item]["type"],host=data["dns"][item]["host"],data=data["dns"][item]["data"])
        #    domain.addDNSRecord(dns)
        domain.postDomainToSendgrid()
        current_user.account.addDomain(domain)
        db.session.add(current_user.account)
        db.session.commit()
    return render_template('settings/domain.html',
                title='Email Configuration',
                account=current_user.account,
                form=form)

@bp.route('/view/domain/<domain_id>', methods=['GET', 'POST'])
def view_domain(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    return render_template('settings/view_domain.html',
                title=domain.domain,
                account=current_user.account,
                domain=domain)

@bp.route('/edit/domain/<domain_id>', methods=['GET', 'POST'])
def edit_domain(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    form = DomainForm(obj=domain)
    if form.validate_on_submit():
        form.populate_obj(domain)
        db.session.add(domain)
        db.session.commit()
        return redirect(url_for('.view_domain', domain_id=domain.id))
    return render_template('settings/domain.html',
                title="Edit {}".format(domain.domain),
                account=current_user.account,
                form=form)

@bp.route('/delete/domain/<domain_id>', methods=['GET', 'POST'])
def delete_domain(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    db.session.delete(domain)
    db.session.commit()
    return redirect(url_for('.email'))

@bp.route('/validate/domain/<domain_id>', methods=['GET', 'POST'])
def validate_domain(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    domain.validate()
    db.session.add(domain)
    db.session.commit()
    return redirect(url_for('.email'))

@bp.route('/profile', methods=['GET','POST'])
def my_profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.add(current_user)
        db.session.commit()
    return render_template('settings/profile.html',
                title="My Profile",
                user=current_user,
                form=form)
