from flask import Flask, render_template, request, redirect, session, url_for, flash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from auth.signup import signup_bp
from auth.login import login_bp

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user, login_manager
import mysql.connector

app = Flask(__name__)
app.register_blueprint(signup_bp, url_prefix='/auth')
app.register_blueprint(login_bp, url_prefix='/auth')

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:badman2001@localhost/waste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#secret key
app.config['SECRET_KEY']= "my secret key"

# Initialize the database
db = SQLAlchemy(app)

# Import models and routes AFTER db initialization to avoid circular imports
from auth.models import User  # Your User model
from auth import init_auth    # Auth blueprint

# Initialize auth module (if using modular structure)
init_auth(app)

# Create the database tables (run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        flash(f"Form submitted! Name: {name}, Email: {email}","success")
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)
    