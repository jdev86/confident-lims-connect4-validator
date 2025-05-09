from flask import Flask
from .routes import api_routes  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register blueprints (routes)
    app.register_blueprint(api_routes)

    return app