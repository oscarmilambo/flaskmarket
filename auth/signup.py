from flask import Blueprint, request, redirect, url_for, flash
from . import auth_bp, db
from .models import User  # Assuming SQLAlchemy
from werkzeug.security import generate_password_hash

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256')
        location = request.form.get('location')  # Kalingalinga, Kanyama, etc.
        language = request.form.get('language')  # English, Bemba, Nyanja
        
        #check if user exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists!')
            return redirect(url_for('auth.signup'))
    
    # Create new user
    new_user = User(
        name=name,
        email=email,
        phone=phone,
        password=generate_password_hash(password),
        location=location,
        language=language
    )
    db.session.add(new_user)
    db.session.commit()

    flash(f'Account created for {name}!','success')
    return redirect(url_for('auth.login'))
    return render_template('signup.html')

