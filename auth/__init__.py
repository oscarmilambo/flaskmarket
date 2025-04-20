from flask import Blueprint

# Create a Blueprint for authentication
auth = Blueprint('auth', __name__)

# Import routes (signup and login)
from auth import signup, login