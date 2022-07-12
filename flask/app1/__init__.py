from flask import Flask
import os

app = Flask(__name__)
app.config['DEBUG'] = os.getenv("DEBUG")
app.config['CORS_HEADERS'] = os.getenv("CORS_HEADERS")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config['SQLALCHEMY_DATABASE_URI'] =os.getenv("SQLALCHEMY_DATABASE_URI")

from .Api.example import api_page as api_blueprint
app.register_blueprint(api_blueprint)