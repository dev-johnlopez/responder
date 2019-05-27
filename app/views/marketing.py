from flask import g, render_template, request, redirect, url_for, g
from flask_security import login_required
from app import db
from app.views import marketing_bp as bp
from app.forms import TemplateForm
from app.models import Template
from app.forms.search import SearchForm

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('marketing/index.html',
                title='Marketing')

@bp.route('/campaigns', methods=['GET', 'POST'])
@login_required
def campaigns():
    return render_template('marketing/index.html',
                title='Marketing')

@bp.route('/templates', methods=['GET', 'POST'])
@login_required
def templates():
    templates = Template.query.all()
    return render_template('marketing/templates.html',
                title='My Marketing Templates',
                templates=templates)

@bp.route('/template/add', methods=['GET', 'POST'])
def create_template():
    form = TemplateForm()
    if form.validate_on_submit():
        template = Template()
        form.populate_obj(template)
        db.session.add(template)
        db.session.commit()
    return render_template('marketing/template_form.html',
                title='New Marketing Templates',
                form=form)

@bp.route('/template/<template_id>')
def view_template(template_id):
    template = Template.query.get_or_404(template_id)
    return render_template('marketing/templates.html',
                title='My Marketing Templates',
                template=template)

@bp.route('/template/<template_id>/edit', methods=['GET', 'POST'])
def edit_template(template_id):
    template = Template.query.get_or_404(template_id)
    form = TemplateForm(obj=template)
    if form.validate_on_submit():
        form.populate_obj(template)
        db.session.add(template)
        db.session.commit()
        return redirect(url_for('.view_template', template_id=template.id))
    return render_template('marketing/template_form.html',
                title='Edit Template',
                form=form)

@bp.route('/template/<template_id>/delete')
def delete_template(template_id):
    template = Template.query.get_or_404(template_id)
    db.session.delete(template)
    db.session.commit()
    return redirect(url_for('marketing.templates'))

@bp.route('/sequences', methods=['GET', 'POST'])
def sequences():
    return render_template('marketing/index.html',
                title='Marketing')
