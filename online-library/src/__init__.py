from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = '1234567891'
    app.config['JWT_SECRET_KEY'] = '1234567891'
    
    db.init_app(app)
    
    
    return app