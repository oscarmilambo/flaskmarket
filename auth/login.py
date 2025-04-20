from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from auth import auth
from models.user import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid email or password!', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')