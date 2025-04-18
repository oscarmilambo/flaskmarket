from flask import Blueprint, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from . import db  # Assuming you have a Flask-SQLAlchemy setup

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.users.filter_by(email=email).first()  # Example for MongoDB/MySQL

        if user and check_password_hash(user.password, password):  # Updated to access password directly
            session['user_id'] = str(user.id)
            session['logged_in'] = True
            flash('Logged in successfully')  # Store user in session, assuming user has an id attribute
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('auth.login')) # Redirect to login page if authentication fails
        
@auth_bp.route('/logout')
def logout():
    # Clear all session variables
    session.pop('logged_in', None)
    session.pop('user_id', None)       # Match your login's session key
    session.pop('username', None)      # Optional (if used)
    flash("You have been logged out.", "success")
    return redirect(url_for('auth.login'))  # Redirect to login page