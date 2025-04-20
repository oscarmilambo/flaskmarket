from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from auth import auth
from models.user import db, User

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        province = request.form.get('province')
        district = request.form.get('district')
        community = request.form.get('community')
        user_type = request.form.get('userType')
        preferred_language = request.form.get('preferredLanguage')

        # Validate form data
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('auth.signup'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Save user to the database
        new_user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            password=hashed_password,
            province=province,
            district=district,
            community=community,
            user_type=user_type,
            preferred_language=preferred_language
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('auth.signup'))

    return render_template('signup.html')