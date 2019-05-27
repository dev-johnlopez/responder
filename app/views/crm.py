from flask import g, render_template, redirect, url_for, g, flash
from flask_security import current_user, login_required
from app import db
from app.models import Contact, Tag, Indicator
from app.views import crm_bp as bp
from app.forms import ContactForm
from app.forms.search import SearchForm
from app.forms.upload import UploadForm
from app.forms.tag import TagForm
from app.forms.indicator import IndicatorForm
#from webob.multidict import MultiDict

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('crm/index.html',
                title='CRM')

@bp.route('/all', methods=['GET', 'POST'])
@login_required
def all_leads():
    contacts = Contact.query.all()
    return render_template('crm/all_contacts.html',
                title='My Contacts',
                contacts=contacts)

@bp.route('/new_lead', methods=['GET', 'POST'])
@login_required
def new_lead():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact()
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('.view_lead', contact_id=contact.id))
    return render_template('crm/edit_contact.html',
                title='New Lead',
                form=form)

@bp.route('<contact_id>/view', methods=['GET', 'POST'])
@login_required
def view_lead(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
    return render_template('crm/view_contact.html',
                title='CRM',
                contact=contact,
                form=form)

@bp.route('<contact_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_lead(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('.view_lead', contact_id=contact.id))
    return render_template('crm/edit_contact.html',
                title='Edit Lead',
                form=form)

@bp.route('<contact_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_lead(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('.all_leads'))

@bp.route('import', methods=['GET', 'POST'])
@login_required
def upload():
    #tags = Tag.query.all()
    #indicators = Indicator.query.all()
    #data = {'tags': tags, 'indicators': indicators}
    form = UploadForm()
    if form.validate_on_submit():
        flash(form.options.data, 'info')
        pass
        #flash(form.data, 'info')
        #flash(form.tags, 'info')
        #for tag in form.tags:
        #    flash('{}: {}'.format(tag.form.id.data, tag.form.enabled.data), 'info')
    flash(form.errors, 'info')
    return render_template('crm/upload.html',
                title='Import Data',
                form=form)
