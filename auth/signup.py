from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from auth import auth
from models.user import db, User

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')  # Ensure this matches the form field name
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        location = request.form.get('location')
        language = request.form.get('language')

        # Validate form data
        if not name or not email or not phone or not location or not language:
            flash('All fields are required!', 'error')
            return redirect(url_for('auth.signup'))

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('auth.signup'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Save user to the database
        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            location=location,
            language=language
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('auth.signup'))

    return render_template('signup.html')