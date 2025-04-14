from flask import Flask, render_template, request, redirect, session, url_for, flash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user, login_manager
import mysql.connector

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:badman2001@localhost/waste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#scret key
app.config['SECRET_KEY']= "my secret key"

# Initialize the database
db = SQLAlchemy(app)

# Create the database tables (run this once)
with app.app_context():
    db.create_all()

# Define the user model
class User(db.Model, UserMixin):
    """A class that represents the user table in the database."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Authenticate the user using SQLAlchemy
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            flash("Login successful!", "success")
            # Redirect to a protected route or home page
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('login'))
        
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists. Please choose another.", "error")
            return redirect(url_for('signup'))

        # Hash the password before saving
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Add the new user to the database
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        flash(f"Form submitted! Name: {name}, Email: {email}","successs")
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug=True)
    