# keep this file even if you don't need traditional views
# as it holds the blueprint app instance
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_mongoengine.wtf import model_form
from .models import Material

app = Blueprint('material', __name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('material/index.html')

@app.route('/create')
def create():
    form = model_form(Material)()
    if form.validate_on_submit():
        material = Material()
        form.populate_obj(material)
        material.save()
        flash("Material created successfully", "success")
        return redirect(url_for('material.index'))
    return render_template('material/create.html', form=form)