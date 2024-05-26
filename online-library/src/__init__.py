from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = '1234567891'
    app.config['JWT_SECRET_KEY'] = '1234567891'
    
    jwt = JWTManager(app)
    
    from src.routers import BP_user, BP_Author
    app.register_blueprint(BP_user)
    app.register_blueprint(BP_Author)
    db.init_app(app)
    
    
    return app