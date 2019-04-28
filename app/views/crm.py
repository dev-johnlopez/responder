from flask import g, render_template, redirect, url_for
from app import db
from app.models import Contact
from app.views import crm_bp as bp
from app.forms import ContactForm

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('crm/index.html',
                title='CRM')

@bp.route('/all', methods=['GET', 'POST'])
def all_leads():
    contacts = Contact.query.all()
    return render_template('crm/all_contacts.html',
                title='My Contacts',
                contacts=contacts)

@bp.route('/new_lead', methods=['GET', 'POST'])
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
def delete_lead(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('.all_leads'))
