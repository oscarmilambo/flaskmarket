from flask import Flask, render_template
from flask import Flask
from config import Config
from models.user import db
from auth import auth

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')

#home route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
