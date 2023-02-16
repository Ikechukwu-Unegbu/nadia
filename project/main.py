from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
from .Services.Helpers import get_user_type

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/dashboard')
@login_required
def dashboard():
    user_type = get_user_type(current_user)
    return render_template('authenticated/dashboard.html')