from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = 'wasaa'
    app.config['JWT_SECRET_KEY'] = 'wasaa'
    jwt = JWTManager(app)
    db.init_app(app)
    
    return app
    