from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask wtf import FlaskForm
from wtform import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user, login_manager
import mysql.connector

app = Flask(__name__)
app.secret_key = "my secret key"  # Required for flash messages

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:badman2001@localhost/waste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#scret key
app.config['SECRET KEY']= "my secret key"

# Initialize the database
db = SQLAlchemy(app)

# Define the user model
class User(db.Model, UserMixin):
    """A class that represents the user table in the database."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self):
        self.username = username
        self.email = email

# Create the database tables (run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        record = cursor.fetchone()
        if record:
            session['logged_in'] = True
            session['username'] = username

        # Authenticate the user
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return render_template('login.html', username=user.username)
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username already exists. Please choose another.", "error")
            return redirect(url_for('signup'))

        # Hash the password before saving
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Add the new user to the database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return f"Form submitted! Name: {name},"

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('login.html'))