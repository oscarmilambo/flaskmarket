from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Blueprint for auth routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Initialize database (if not already in app.py)
db = SQLAlchemy()

# Import routes (avoid circular imports)
from . import login, signup, models

def init_auth(app):
    """Initialize auth module with the Flask app."""
    db.init_app(app)
    app.register_blueprint(auth_bp)