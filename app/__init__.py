from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['ENV'] = os.getenv('FLASK_ENV','production')
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app