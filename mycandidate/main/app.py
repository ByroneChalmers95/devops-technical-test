import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_minify import Minify

# Create Flask app
app = Flask(__name__, static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "SECRET_KEY")

# Config
env = os.environ.get("FLASK_ENV", "development")
app.config["ENV"] = env
app.config.from_pyfile(f"config/{env}.cfg", silent=True)

# Database setup
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
db = SQLAlchemy(app)

# Security
csrf_protect = CSRFProtect(app)
app.config["WTF_CSRF_ENABLED"] = False

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Minify responses
Minify(app=app, passive=True)

# Import routes and APIs AFTER app/db are created
from main import routes
from main.api import api_bp

# Register API blueprint
app.register_blueprint(api_bp, url_prefix="/api/v1")

# Expose for Gunicorn
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
