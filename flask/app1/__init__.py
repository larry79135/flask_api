from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@localhost:5432/postgres"

from .Api.example import api_page as api_blueprint
app.register_blueprint(api_blueprint)