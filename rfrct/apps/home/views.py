# keep this file even if you don't need traditional views
# as it holds the blueprint app instance
from flask import Blueprint
from flask import render_template, flash, redirect, url_for

app = Blueprint('home', __name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')