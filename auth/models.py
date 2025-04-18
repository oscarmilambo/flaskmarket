from app import db

class User(db.Model):
    """A class that represents the user table in the database."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(200))  # Hashed
    location = db.Column(db.String(50))   # For geo-targeted content
    language = db.Column(db.String(20))   # English/Bemba/Nyanja
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())