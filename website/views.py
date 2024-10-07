from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint("views", __name__)


################################ pip install sha256
################################ START
@views.route("/")
def index():
    return render_template("index.html", user=current_user)
################################
@views.route("/app", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("/dashboard/dashboard.html", user=current_user)
################################
@views.route('/update-name', methods=['POST'])
@login_required
def update_name():
    new_first_name = request.form.get('firstName')
    
    if new_first_name and len(new_first_name) > 1:
        current_user.first_name = new_first_name
        db.session.commit()
        flash('First name updated successfully!', category='success')
    else:
        flash('First name must be greater than 1 character.', category='error')

    return redirect(url_for('views.dashboard'))
################################